'''
  File name: carv.py
  Author:
  Date created:
'''

'''
  File clarification:
    Aimed to handle finding seams of minimum energy, and seam removal, the algorithm
    shall tackle resizing images when it may be required to remove more than one seam, 
    sequentially and potentially along different directions.


Utilizing recursive calls of the functions completed in the previous 2 tasks, 
    complete this function to output the resized image.
    
    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT nr: the numbers of rows to be removed from the image.
    - INPUT nc: the numbers of columns to be removed from the image.
    - OUTPUT Ic: (n − nr) × (m − nc) × 3 matrix representing the carved image.
    - OUTPUT T: (nr + 1) × (nc + 1) matrix representing the transport map.
'''
from genEngMap import genEngMap
from cumMinEngHor import cumMinEngHor
from cumMinEngVer import cumMinEngVer
from rmVerSeam import rmVerSeam
from rmHorSeam import rmHorSeam

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import imageio

class Im:
  def __init__(self, Img, r, c):
    self.Img = np.zeros((r, c, 3))
    self.Img = Img

def carv(I, nr, nc):

  # transport map
  T = np.zeros((nr + 1, nc + 1))

  # array of images
  Im_array = np.empty((nr + 1, nc + 1), dtype = Im)

  # first spot is the original image I
  Im_array[0, 0] = Im(I, I.shape[0], I.shape[1]) 

  # vertical edge case - first row of T matrix 
  I_copy = np.copy(I) # create a copy of the image (I had referencing issues)
  for j in range(1, nc + 1):
    # recompute energy map
    e = genEngMap(I_copy)

    # compute cumulative minimum energy (vertical)
    Vx, P = cumMinEngVer(e)
    I_copy, E = rmVerSeam(I_copy, Vx, P)

    # store cumulative energy in Transport map
    T[0, j] = E + T[0, j - 1]

    # store each image in the image array
    Im_array[0, j] = Im(I_copy, I.shape[0], I.shape[1])

  # horizontal edge case - first column of T matrix
  I_copy = np.copy(I) # create a copy of the image (I had referencing issues)
  for i in range(1, nr + 1):
    # recompute energy map
    e = genEngMap(I_copy)
    
    # compute cumulative minimum energy (horizontal)
    Vy, P = cumMinEngHor(e)

    # remove the horizontal seam
    I_copy, E = rmHorSeam(I_copy, Vy, P)

    # store cumulative energy in Transport map
    T[i, 0] = E + T[i - 1,0]

    # store each image in the image array
    Im_array[i, 0] = Im(I_copy, I.shape[0], I.shape[1])

  for i in range(1, nr + 1):
    for j in range(1, nc + 1):
      # vertical seam computation
      I_vert = np.copy(Im_array[i, j - 1].Img)
      e_vert = genEngMap(I_vert)
      Vx, Px = cumMinEngVer(e_vert)
      I_vert, E_vert = rmVerSeam(I_vert, Vx, Px)

      # horizontal seam computation
      I_hor = np.copy(Im_array[i - 1, j].Img)   
      e_hor = genEngMap(I_hor)
      Vy, Py = cumMinEngHor(e_hor)
      I_hor, E_hor = rmHorSeam(I_hor, Vy, Py)
      
      # hor Energy  < vert energy
      if(E_hor < E_vert):
        T[i, j] = T[i - 1, j] + E_hor
        Im_array[i, j] = Im(I_hor, I.shape[0], I.shape[1])

      # vert Energy  <= hor energy
      else:
        T[i, j] = T[i, j - 1] + E_vert
        Im_array[i, j] = Im(I_vert, I.shape[0], I.shape[1])


  # array of images
  Im_array_gif = np.zeros((nr + nc + 1), dtype = Im)
  Im_array_gif[0] = Im_array[nr,nc]
  res_list = [] # used for the gif

  # trace back through T to create the .gif
  counter = 1
  i = nr
  j = nc

  # add lower energies to the array of images for the gif
  while (i > 0 or j > 0):
    if(T[i, j-1] < T[i-1, j]):
      Im_array_gif[counter] = Im_array[i,j]
      j = j - 1

    else:
      Im_array_gif[counter] = Im_array[i,j]
      i = i - 1 
    counter = counter + 1    

  k = nr+nc
  while k >= 0: # decrement backwards to start at the original image
    res_list.append(Im_array_gif[k].Img[:, :, :]/255.)
    k -= 1

  
  # generate gif file
  imageio.mimsave('./seaming.gif', res_list)

  Ic = Im_array[nr, nc].Img

  return Ic, T


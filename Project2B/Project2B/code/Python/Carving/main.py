'''
  File name: main.py
  Author: Marissa Como
  Date created: 10/18/2018
'''
from PIL import Image
import os
import numpy as np
from carv import carv
import matplotlib.pyplot as plt


from genEngMap import genEngMap
from cumMinEngHor import cumMinEngHor
from cumMinEngVer import cumMinEngVer
from rmVerSeam import rmVerSeam
from rmHorSeam import rmHorSeam

def main():

  #  import image
  im_path = os.path.join('images',"mom.PNG")  #"plane.jpg") # "ben.png")  #"im_from_lecture.JPG") 
  I = np.array(Image.open(im_path).convert('RGB'))

  # number of rows and columns to delete
    # image from lecture slides
#  nr = 2
 # nc = 20

  # ben
#  nr = 2
#  nc = 20

  # mom
  nr = 10
  nc = 15

  # plane
 # nr = 4
 # nc = 22

  # image carving 
  Ic, T = carv(I, nr, nc)

  plt.imshow(I)
  plt.title("original")
  plt.show()

  plt.imshow(Ic/255.)
  plt.title("carved")
  plt.show()

  fig = plt.figure()
  plt.subplot(221)
  plt.title("original - shape: " + str(I.shape))
  plt.imshow(I)

  plt.subplot(222)
  plt.imshow(Ic/255.)
  plt.title("carved - shape: " + str(Ic.shape))
  plt.show()

  return 
if __name__ == "__main__":
  main()

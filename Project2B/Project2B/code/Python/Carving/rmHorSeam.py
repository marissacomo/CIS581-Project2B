'''
  File name: rmHorSeam.py
  Author:
  Date created:
'''

'''
  File clarification:
    Removes horizontal seams. You should identify the pixel from My from which 
    you should begin backtracking in order to identify pixels for removal, and 
    remove those pixels from the input image. 
    
    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT My: n × m matrix representing the cumulative minimum energy map along horizontal direction.
    - INPUT Tby: n × m matrix representing the backtrack table along horizontal direction.
    - OUTPUT Iy: (n − 1) × m × 3 matrix representing the image with the row removed.
    - OUTPUT E: the cost of seam removal.
'''
import numpy as np
def rmHorSeam(I, V, P):
  n = I.shape[0] # n x m-1 x 3 matrix
  m = I.shape[1]
  Iy = np.zeros((n-1, m, 3))

  #n = V.shape[0] # n x m-1 x 3 matrix
  #m = V.shape[1]

  # get last col of value matrix
  colValue = V[:, m-1] 
  minIndex = np.argmin(colValue) # find index of minimum value in last row of value matrix
  E = V[minIndex, m-1] # total cost of seam removal

  for j in range(m, 0, -1):
    dirP = P[minIndex, j-1] # where to go
    pixeltoDelIndex_i = minIndex + dirP  # j index of pixel to delete

    # get the col in the image
    colImageR = I[:, j-1, 0] # R 
    colImageG = I[:, j-1, 1] # G 
    colImageB = I[:, j-1, 2] # B 

    colyR = np.delete(colImageR, minIndex) # delete col
    colyG = np.delete(colImageG, minIndex)
    colyB = np.delete(colImageB, minIndex)

    Iy[:, j-1, 0] = colyR # copy col to in Iy
    Iy[:, j-1, 1] = colyG 
    Iy[:, j-1, 2] = colyB 

    minIndex = int(pixeltoDelIndex_i)
     
  return Iy, E

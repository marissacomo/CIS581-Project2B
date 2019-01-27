'''
  File name: rmVerSeam.py
  Author:
  Date created:
'''

'''
  File clarification:
    Removes vertical seams. You should identify the pixel from My from which 
    you should begin backtracking in order to identify pixels for removal, and 
    remove those pixels from the input image. 
    
    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT V? Mx: n × m matrix representing the cumulative minimum energy map along vertical direction.
    - INPUT P? Tbx: n × m matrix representing the backtrack table along vertical direction.
    - OUTPUT Ix: n × (m - 1) × 3 matrix representing the image with the row removed.
    - OUTPUT E: the cost of seam removal.
'''
import numpy as np
import matplotlib.pyplot as plt

def rmVerSeam(I, V, P):
  n = I.shape[0] # n x m-1 x 3 matrix
  m = I.shape[1]
  Ix = np.zeros((n, m-1, 3))

  # get last row of value matrix
  rowValue = V[n-1,:] 
  minIndex = np.argmin(rowValue) # find index of minimum value in last row of value matrix
  E = V[n-1, minIndex] # total cost of seam removal

  for i in range(n, 0, -1):
    dirP = P[i-1, minIndex] # where to go
    pixeltoDelIndex_j = minIndex + dirP  # j index of pixel to delete

    # get the last row in the image
    rowImageR = I[i-1, :, 0] # R 
    rowImageG = I[i-1, :, 1] # G
    rowImageB = I[i-1, :, 2] # B 

    rowxR = np.delete(rowImageR, minIndex) # delete row
    rowxG = np.delete(rowImageG, minIndex)
    rowxB = np.delete(rowImageB, minIndex)

    Ix[i-1,:, 0] = rowxR # copy row to in Ix
    Ix[i-1,:, 1] = rowxG 
    Ix[i-1,:, 2] = rowxB 

    minIndex = int(pixeltoDelIndex_j)

  # Your Code Here 
  return Ix, E

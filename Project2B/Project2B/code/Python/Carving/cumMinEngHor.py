'''
  File name: cumMinEngHor.py
  Author:
  Date created:
'''

'''
  File clarification:
    Computes the cumulative minimum energy over the horizontal seam directions.

    - INPUT e: n × m matrix representing the energy map.
    - OUTPUT V? My: n × m matrix representing the cumulative minimum energy map along horizontal direction.
    - OUTPUT P? Tby: n × m matrix representing the backtrack table along horizontal direction.
'''
import numpy as np 
from scipy.ndimage.interpolation import shift

def cumMinEngHor(e):
  n = e.shape[0] # nxm matrix
  m = e.shape[1]
  V = np.zeros((n,m)) # Value matrix
  P = np.zeros((n,m)) # Path matrix
  
  V[:,0] = e[:,0] # initilize 1st row

  # use to get pixels before and after in the row above
  Y = np.arange(0, n)
  Y_b = np.clip(Y + 1, 0, n-1) # before
  Y_a = np.clip(Y - 1, 0, n-1) # after

  # grow the frontier
  for j in range(1, m):
    col = V[:,j-1].copy()
    shift_right = col[Y_a]
    shift_left = col[Y_b]

    result = np.less(shift_right, col[Y])   
    col[result] = shift_right[result] 
    P[result,j] = 1
    
    result1 = np.less(shift_left, col[Y])
    col[result1] = shift_left[result1]
    P[result1,j] = -1

    v_col = e[:,j] + col[Y]
    V[:,j] = v_col

  return V, P

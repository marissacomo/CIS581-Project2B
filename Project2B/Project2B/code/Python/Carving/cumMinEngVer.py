'''
  File name: cumMinEngVer.py
  Author:
  Date created:
'''

'''
  File clarification:
    Computes the cumulative minimum energy over the vertical seam directions.

    - INPUT e: n × m matrix representing the energy map.
    - OUTPUT Mx: n × m matrix representing the cumulative minimum energy map along vertical direction.
    - OUTPUT Tbx: n × m matrix representing the backtrack table along vertical direction.
'''
import numpy as np
def cumMinEngVer(e):
  n = e.shape[0] # nxm matrix
  m = e.shape[1]
  V = np.zeros((n,m)) # Value matrix
  P = np.zeros((n,m)) # Path matrix
  
  V[0,:] = e[0,:] # initilize 1st row
  P[0] = 0

  # use to get pixels before and after in the row above
  X = np.arange(0,m)
  X_b = np.clip(X - 1, 0, m-1) # before
  X_a = np.clip(X + 1, 0,m-1) # after

  # grow the frontier
  for i in range(1, n):
    row = V[i-1].copy()
    shift_right = row[X_a]
    shift_left = row[X_b]

    result = np.less(shift_right, row[X])    
    row[result] = shift_right[result]
    P[i,result] = 1

    result1 = np.less(shift_left, row[X])
    row[result1] = shift_left[result1]
    P[i,result1] = -1

    v_row = e[i, :] + row[X]
    V[i] = v_row

  return V, P

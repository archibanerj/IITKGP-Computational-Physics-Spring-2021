import numpy as np
import solveLinear as sol

"""
Equations for the junctions:

  4V1 - V2 - V3 - V4  = 5
  V1 -3V2 + 0V3 + V4  = 0
  V1 + V2 + V3 - 4V4  = 0
-1V1 + 0V2 + 3V3 - V4 = 5
"""

A = [[4,-1,-1,-1],[1,-3,0,1],[1,1,1,-4],[-1,0,3,-1]]
temp = np.array(A.copy(),float)
b = [[5],[0],[0],[5]]

A = np.array(A,float)
b = np.array(b,float)

A,b = sol.gaussElim(A,b)
print("Upper Triangular Form of Matrix: ")
print(A)

solution = sol.backsubs(A,b)

print("Solution of the system\n", solution)

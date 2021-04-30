import numpy as np
import gaussJordan as gj

A = [[0,2,0,1],[2,2,3,2],[4,-3,0,1],[6,1,-6,-5]]
temp = A.copy()
b = [[0],[-2],[-7],[6]]

A = np.array(A,float)
b = np.array(b,float)

A,b = gj.pivot_solve(A,b)


print("Solution of the system\n", b)

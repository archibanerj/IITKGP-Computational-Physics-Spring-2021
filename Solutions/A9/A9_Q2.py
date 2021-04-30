import numpy as np
import solveLinear as sol

A = [[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]]
b = [[-4],[3],[9],[7]]

A = np.array(A,float)
b = np.array(b,float)

A,b = sol.gaussElim(A,b)
print("Upper Triangular Form of Matrix: ")
print(A)

solution = sol.backsubs(A,b)

print("Solution of the system\n", solution)

import numpy as np
import matplotlib.pyplot as plt

def initialise(D,V_top): #Initialises the problem domain
    n = len(D)
    D[0] = V_top
    return D

def jacobi(D):
    count = 0
    flag = 0
    while flag==0:
        count += 1
        temp = D.copy()
        for i in range(1,len(D)-1):
            for j in range(1,len(D)-1):
                D[i][j] = 0.25*(D[i-1][j]+D[i][j-1]+D[i+1][j]+D[i][j+1])

        diff = abs(temp.copy() - D.copy())
        flag = 1
        for i in range(len(D)):
            for j in range(len(D)):
                if diff[i][j] > 10e-5 :
                    flag = 0
                    break
            if flag == 0:
                break

    return D

grids = int(input("Enter the number of grids along axes: "))
D = np.zeros((grids,grids),float)
V_top = float(input("Enter the potential on the top face: "))
D = initialise(D,V_top)
D = jacobi(D)
plt.imshow(D)
plt.show()
#Make a 3D plot!

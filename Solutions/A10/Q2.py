import numpy as np
import matplotlib.pyplot as plt


def jacobi(D,Q,interval):
    count = 0
    flag = 0
    while flag==0:
        count += 1
        temp = D.copy()
        for i in range(1,len(D)-1):
            for j in range(1,len(D)-1):
                D[i][j] = 0.25*((D[i-1][j]+D[i][j-1]+D[i+1][j]+D[i][j+1])+(interval**2)*Q[i][j]/4)

        diff = abs(temp.copy() - D.copy())
        flag = 1
        for i in range(len(D)):
            for j in range(len(D)):
                if diff[i][j] > 10e-5 :
                    flag = 0
                    break
            if flag == 0:
                break

    return D,count

grids = int(input("Enter the number of grids along axes: "))
l = 100 #100 cm
D = np.zeros((grids,grids),float)
dx = l/(grids)

q = float(input("Enter charge: "))

Q = np.zeros((grids,grids),float)
Q[20][20] =   q/(dx**2) #Surface charge density
Q[80][80] = - Q[20][20]

D,iter = jacobi(D,Q,dx)
plt.pcolor(D)
plt.show()

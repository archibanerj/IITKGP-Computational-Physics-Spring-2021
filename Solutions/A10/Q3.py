import numpy as np
import matplotlib.pyplot as plt

def init(A,L,dx):
    L = 10 #taken to be 10 by default

    #from x=2 cm and y=2 cm to x = 2 cm and y = 8 cm there is a fixed 1 V capacitor
    #Same for x=8 cm
    l = int(2/dx)
    u = int(8/dx)

    for i in range(l,u+1):
        A[i][l] = 1

    for i in range(l,u+1):
        A[i][u] = -1

    return A

def solve(A,L,dx):
    L = 10 #taken to be 10 by default
    l = int(2/dx)
    u = int(8/dx)

    count = 0
    flag = 0
    while flag==0:
        count += 1
        temp = A.copy()

        for i in range(1,len(A)-1):
            for j in range(1,len(A)-1):
                if i >= l:
                    if i <= u:
                        if j!=l:
                            if j!=u:
                                A[i][j] = 0.25*(A[i-1][j]+A[i][j-1]+A[i+1][j]+A[i][j+1])
                    else:
                        A[i][j] = 0.25*(A[i-1][j]+A[i][j-1]+A[i+1][j]+A[i][j+1])
                else:
                    A[i][j] = 0.25*(A[i-1][j]+A[i][j-1]+A[i+1][j]+A[i][j+1])


        diff = abs(temp.copy() - A.copy())
        flag = 1
        for i in range(len(A)):
            for j in range(len(A)):
                if diff[i][j] > 10e-6 :
                    flag = 0
                    break
            if flag == 0:
                break

    return A,count

#number of intervals we are using to discretise both axes
intervals = int(input("Enter the number of intervals along x axis/y axis: "))
grids = intervals + 1 #number of grid points along an axis
Potential = np.zeros((grids,grids),float)

L = 10 #in cm
dx = L/intervals

Potential = init(Potential,L,dx).copy() #Initialises the boundary value problem

Potential,iter = solve(Potential,L,dx)

"""
x = np.linspace(0,10,grids)
y = np.linspace(0,10,grids)
X,Y = np.meshgrid(x,y)
ax_1 = plt.axes(projection = '3d')
ax_1.plot_wireframe(X,Y,Potential) #how to put colors?
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()
"""

plt.pcolor(Potential)
plt.show()

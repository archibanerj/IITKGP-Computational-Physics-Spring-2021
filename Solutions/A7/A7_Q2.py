import numpy as np
import matplotlib.pyplot as plt

def func(x,y):
    return np.sin(x+y) + np.cos(x+y)

def interpolate(x,y,samples_x,samples_y) :
    #x,y - domain point at which we have to find the value of the interpolated polynomial
    #samples_x, samples_y - the points at which the values of original function have been sampled
    nx = len(samples_x)
    ny = len(samples_y)
    term = 1
    sum = 0
    for i in range(nx):
        for j in range(ny):
            for p in range(nx):
                if p!=i:
                    term *= ((x - samples_x[p])/(samples_x[i]-samples_x[p]))
            for q in range(ny):
                if q!=j:
                    term *= ((y - samples_y[q])/(samples_y[j]-samples_y[q]))
            sum += term*func(samples_x[i],samples_y[j])
            term = 1
    return sum

x = np.linspace(0,np.pi,10)
y = np.linspace(0,np.pi,10)

print('Enter the values of (x0,y0) for evaluating interpolating polynomial')
x0 = float(input("Enter x0 "))
y0 = float(input("Enter y0 "))

print("Value calculated from original function: ",func(x0,y0))
print("Value calculated using interpolated polynomial: ",interpolate(x0,y0,x,y))
#For the point (1,2), x0 = 1 and y0 = 2 & value obtained from interpolation: -0.84887248

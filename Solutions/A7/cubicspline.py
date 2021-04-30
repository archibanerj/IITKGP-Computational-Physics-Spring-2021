"""
In this code, you will have to input the x and y values
through which a cubic spline is to be interpolated.

We will use natural spline interpolation and assume
y"[0] = y"[N-1] = 0

This will result in N-2 linear equations which we will
first simplify, and then solve

"""

import numpy as np
from numpy import linalg

#x and y are numpy arrays containing the data points
def double_primes(x,y):
    N = len(x)
    A = np.zeros(shape = (N-2,N-2))
    B = np.zeros(N-2)

    #Now, we will construct the equations by creating the A and B
    i = 1
    while i<=N-2:
        #Filling A matrix
        a = (1/6)*(x[i] - x[i-1])
        b = (1/3)*(x[i+1] - x[i-1])
        c = (1/6)*(x[i+1] - x[i])

        if i != 1:
            A[i-1][i-2] = a

        A[i-1][i-1] = b

        if i != N-2:
            A[i-1][i] = c

        #Filling B vector

        d = ((y[i+1]-y[i])/(x[i+1]-x[i]))-((y[i]-y[i-1])/(x[i]-x[i-1]))
        B[i-1] = d
        i += 1

    y_doubprime = np.dot(linalg.inv(A),B)
    y_doubprime = list(y_doubprime)
    y_doubprime.append(0)
    y_doubprime.insert(0,0)
    return y_doubprime

def interpolate(x,samples,values,y_doubprime):

    i = 0
    while x>samples[i+1]:
        i += 1
        if i == len(samples) - 1:
            return values[i]

    A = (samples[i+1]-x)/(samples[i+1]-samples[i])
    B = (x - samples[i])/(samples[i+1]-samples[i])
    C = (1/6)*((A**3) - A)*((samples[i+1]-samples[i])**2)
    D = (1/6)*((B**3) - B)*((samples[i+1]-samples[i])**2)
    y = A*values[i] + B*values[i+1] + C*y_doubprime[i] + D*y_doubprime[i+1]

    return y

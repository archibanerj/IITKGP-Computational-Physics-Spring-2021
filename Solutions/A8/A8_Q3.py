import numpy as np

def interpolate(x,domain,f):

    term = 0
    sum = 0
    for i in range(len(domain)):
        term = 1
        for j in range(len(domain)):
            if i!=j:
                term *= (x - domain[j])/(domain[i]-domain[j])
        sum += term*f[i]

    return sum

X = np.array([1 , 1.1 , 1.2 , 1.3 , 1.4])
Y = np.array([0.54030 , 0.45360 ,  0.363236 , 0.26750 , 0.16997])

print("Value at x = 1.27 from lagrange interpolation: ", interpolate(1.27,X,Y))

import numpy as np
import matplotlib.pyplot as plt
import cubicspline as cs

def lagrange(x,domain,values):
    sum = 0
    term = 1
    N = len(domain)

    for i in range(N):
        term = 1
        for j in range(N):
            if i!=j:
                term *= (x - domain[j])/(domain[i]-domain[j])
        sum += term*values[i]
    return sum

D = np.array([1.0,2.1,5.0])
V = np.array([8.0,20.6,13.7])

N=100
X = np.linspace(1,5,N)
Y_cubic = np.zeros(N)
Y_lagrange = np.zeros(N)


for i in range(N):
    Y_cubic[i] = cs.interpolate(X[i],D,V,cs.double_primes(D,V))
    Y_lagrange[i] = lagrange(X[i],D,V)


plt.plot(X,Y_lagrange,label = 'Lagrange interpolation')
plt.plot(X,Y_cubic,label = 'Cubic Spline interpolation')
plt.scatter(D,V, label = 'Given Values')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.savefig("Q4.png")
plt.show()

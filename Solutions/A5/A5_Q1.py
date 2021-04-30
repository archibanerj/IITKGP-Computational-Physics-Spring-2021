import numpy as np
import matplotlib.pyplot as plt

def func(X) :
    return 1 + 0.5 * np.tanh(2*X)

#setting the number of discrete points and defining the domain
N=100
domain = np.linspace(-2,2,N)

#defining the infinitesimal segment
dx = float(4/(N-1))

#defining the necessary arrays
f = func(domain)
f_prime = np.zeros(N);
f_prime_theo = np.cosh(2*domain)**-2

#calculating the f_prime array using central difference scheme
for i in range(N) :
    if (i>0)&(i<N-1):
        f_prime[i] = (f[i+1] - f[i-1])/(2*dx)


#plotting the numerical and theoretical data
plt.plot(domain,f,label = 'f(x)')
plt.scatter(domain,f_prime, label = 'Numerical f\'(x)')
plt.plot(domain,f_prime_theo, label = 'Theoretical f\'(x)')
plt.legend()
plt.savefig('Question 1 Plot')
plt.show()

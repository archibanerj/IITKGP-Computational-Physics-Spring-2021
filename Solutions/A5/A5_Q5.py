import numpy as np
import matplotlib.pyplot as plt

def J(m,x):
    N = 1000 #number of points
    theta = np.linspace(0,np.pi,N) #setting up the domain of the problem
    dx = np.pi/(N-1)
    f = np.cos(m*theta - x*np.sin(theta)) #integrand of Bessel Function
    integral = (np.sum(f) - (f[0]+f[N-1])/2)*dx
    #Equation of Trapezoid rule: h*(sum of values of f excluding boundary points + 0.5*(f(a)+f(b)))
    #sum of values of f excluding boundary points: sum of all f values - f(a) - f(b)
    return integral/np.pi

X = np.linspace(0,20,100)
J_0 = np.zeros(100)
J_1 = np.zeros(100)
J_2 = np.zeros(100)

for i in range(100):
    J_0[i] = J(0,X[i])
    J_1[i] = J(1,X[i])
    J_2[i] = J(2,X[i])

plt.plot(X,J_0,label = 'J(0,x)')
plt.plot(X,J_1,label = 'J(1,x)')
plt.plot(X,J_2,label = 'J(2,x)')
plt.legend()
plt.savefig('Question 5 Plot')
plt.show()

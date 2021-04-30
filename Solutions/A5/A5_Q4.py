import matplotlib.pyplot as plt
import numpy as np

def func(t) :
    return np.e**(-(t**2))

def E(x):
    delta = 0.1
    N = int(x/delta) + 1 #total number of points
    domain = np.linspace(0,x,N) #defining the domain of integration

    f = func(domain)
    #Equation of Trapezoid rule: h*(sum of values of f excluding boundary points + 0.5*(f(a)+f(b))
    #sum of values of f excluding boundary points: sum of all f values - f(a) - f(b)
    return (np.sum(f) - (f[0]+f[N-1])/2)*delta

x = 3

print("Integral at x=3 : ",E(x)) #Output: 0.886206734

#plotting the integral as a function of X
N = 10*x+1
X = np.linspace(0,x,N)
Y = np.zeros(N)
for i in range(N):
   Y[i] = E(X[i])
plt.plot(X,Y) #The output comes as the positive part of the erf function
plt.savefig('Question 4 Plot')
plt.show()

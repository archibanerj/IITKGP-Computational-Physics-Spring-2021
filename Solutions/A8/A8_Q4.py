import numpy as np
import matplotlib.pyplot as plt

def f1(x): #True value - 0.5
    return x

def f2(x): #True Value - 0.3333
    return x**2

def f3(x): #True value - 2
    return np.sin(x)

def f4(x):
    return x**4 - 2*x + 1

def trapezoidal(domain,f):
    h = domain[1] - domain[0]

    return h*(2*np.sum(f) - f[0] - f[len(f)-1])/2

def simpson(domain,f):
    h = domain[1] - domain[0]
    even = []
    odd  = []
    for i in range(len(domain)):
        if (i != 0) & (i != len(domain)-1) :
            if i%2 == 0:
                even.append(f[i])
            else :
                odd.append(f[i])

    return (1/3)*(4*np.sum(odd) + 2*np.sum(even) + f[0] + f[len(f) -1])*h

#Number of points in simpson's rule has to be odd, as the intervals have to be even

integrand_simp1 = []
integrand_trap1 = []
integrand_simp2 = []
integrand_trap2 = []
integrand_simp3 = []
integrand_trap3 = []

N_domain = np.linspace(2,100,50)

for i in range(2,101,2):
    N = i + 1 #Number of points
    domain1 = np.linspace(0,1,N)
    domain2 = np.linspace(0,np.pi,N)
    Y1 = f1(domain1)
    Y2 = f2(domain1)
    Y3 = f3(domain2)

    integrand_simp1.append(simpson(domain1,Y1))
    #print(simpson(domain1,Y1))

    integrand_trap1.append(trapezoidal(domain1,Y1))
    #print(trapezoidal(domain1,Y1))


    integrand_simp2.append(simpson(domain1,Y2))
    integrand_trap2.append(trapezoidal(domain1,Y2))

    integrand_simp3.append(simpson(domain2,Y3))
    integrand_trap3.append(trapezoidal(domain2,Y3))


integrand_simp1 = np.array(integrand_simp1)
integrand_trap1 = np.array(integrand_trap1)
integrand_simp2 = np.array(integrand_simp2)
integrand_trap2 = np.array(integrand_trap2)
integrand_simp3 = np.array(integrand_simp3)
integrand_trap3 = np.array(integrand_trap3)

error_simp1 = abs((integrand_simp1 - 0.5)/0.5)
error_simp2 = abs((integrand_simp2 - (1/3))*3)
error_simp3 = abs((integrand_simp3 - 2)/2)

error_trap1 = abs((integrand_trap1 - 0.5)/0.5)
error_trap2 = abs((integrand_trap2 - (1/3))*3)
error_trap3 = abs((integrand_trap3 - 2)/2)

fig, P = plt.subplots(2,1)
P[0].plot(N_domain,error_simp1,label = 'Simpson on x')
P[0].plot(N_domain,error_simp2,label = 'Simpson on x^2')
P[0].plot(N_domain,error_simp3,label = 'Simpson on sin x')


P[1].plot(N_domain,error_trap1,label = 'Trapezoidal on x')
P[1].plot(N_domain,error_trap2,label = 'Trapezoidal on x^2')
P[1].plot(N_domain,error_trap3,label = 'Trapezoidal on sin x')

fig.tight_layout()
P[0].legend()
P[1].legend()
plt.show()

#Explain the results

"""
The graphs show that the error in simpson method is much lesser than in
Trapezoidal rule. It is also observed that with increasing number of
points N, the errors reduce to zero.

On top of that,the errors are exactly zero for x and x^2
in simpson's rule as both those functions can be represented as a general
quadratic function ax^2 + bx + c .

Now, for f(x) = x also gives zero error in trapezoidal rule
as f(x) = x exactly traces out a trapezoidal area in the x-y plane

Thus, the final results match our theroretical understanding of these
methods.
"""

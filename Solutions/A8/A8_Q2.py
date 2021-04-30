import numpy as np
import matplotlib.pyplot as plt

a = 1.0
z_0 = 10.0

def LHS(z) :
    return np.tan(a*z)

def RHS(z) :
    return 2*abs(z)*(np.sqrt(z_0**2 - z**2))/(2*z**2 - z_0**2)

def func(x):
    return LHS(x) - RHS(x)

def bisection(l,u):
    if abs(func(l)) <= 1e-8:
        return l
    elif func(l)*func(u) < 0:
        if func((l+u)/2)*func(u) < 0:
            return bisection((l+u)/2, u)
        else :
            return bisection(l, (l+u)/2)
    elif func(l)*func(u) == 0:
        if func(l) == 0:
            return l
        return u


domain1 = np.linspace(-10,-8,1000)
domain2 = np.linspace(-4.17,-np.pi,1000)
domain3 = np.linspace(-1,1,1000)
domain4 = np.linspace(2.4,3,1000)
domain5 = np.linspace(5,6,1000)
domain6 = np.linspace(3*np.pi,10,1000)

LHS1 = LHS(domain1)
RHS1 = RHS(domain1)
LHS2 = LHS(domain2)
RHS2 = RHS(domain2)
LHS3 = LHS(domain3)
RHS3 = RHS(domain3)
LHS4 = LHS(domain4)
RHS4 = RHS(domain4)
LHS5 = LHS(domain5)
RHS5 = RHS(domain5)
LHS6 = LHS(domain6)
RHS6 = RHS(domain6)

fig, P = plt.subplots(2,3)

P[0][0].plot(domain1,LHS1, label = 'LHS')
P[0][1].plot(domain2,LHS2, label = 'LHS')
P[0][2].plot(domain3,LHS3, label = 'LHS')
P[1][0].plot(domain4,LHS4, label = 'LHS')
P[1][1].plot(domain5,LHS5, label = 'LHS')
P[1][2].plot(domain6,LHS6, label = 'LHS')

P[0][0].plot(domain1,RHS1, label = 'RHS')
P[0][1].plot(domain2,RHS2, label = 'RHS')
P[0][2].plot(domain3,RHS3, label = 'RHS')
P[1][0].plot(domain4,RHS4, label = 'RHS')
P[1][1].plot(domain5,RHS5, label = 'RHS')
P[1][2].plot(domain6,RHS6, label = 'RHS')

fig.tight_layout()

P[0][0].legend()
P[0][1].legend()
P[0][2].legend()
P[1][0].legend()
P[1][1].legend()
P[1][2].legend()

plt.show()

"""
The initial brackets for the first three bound states:

(-1,1)
(2.4,2.8)
(-4,-3.5)
"""

z = np.array([bisection(-1,1),bisection(2.4,2.8),bisection(-4,-3.5)])

E = z**2 - 100

print("The three roots are: ",z[0],z[1],z[2])
print("The three bound state energies in units of h_cross^2/2*m: ",E[0],E[1],E[2])

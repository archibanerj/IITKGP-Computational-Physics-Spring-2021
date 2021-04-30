# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 16:06:04 2021

@author: Archi
"""

from gaussxw import gaussxw
import numpy as np
import matplotlib.pyplot as plt
import math as m


def H(n,x):
    if n==0 :
        return 1
    elif n==1 :
        return 2*x
    else:
        return 2*x*H(n-1,x) - 2*(n-1)*H(n-2,x)

def SHO(n,x):
    K = (2**n)*m.factorial(n)*m.sqrt(m.pi)
    K = K**(-0.5)
    shi = K*np.e**(-(x**2)/2)*H(n,x)
    return shi

def func(n,x):
    Y = SHO(n,(x)/(1-x))**2
    Y = Y*(x**2)*((1-x)**-4)
    return Y

def integral(n):
    x,w = gaussxw(100)
    
    a = 0
    b = 1
    
    xp = 0.5*(b-a)*x + 0.5*(b+a)
    wp = 0.5*(b-a)*w
    
    i = 0
    sum = i 
    
    while i<100:
        sum = sum + wp[i]*func(n,xp[i])
        i = i + 1
    return 2*sum

domain = np.linspace(-4,4,1000)
j=0
f0 = np.zeros(1000)
f1 = np.zeros(1000)
f2 = np.zeros(1000)
f3 = np.zeros(1000)

while j<1000:
    f0[j] = SHO(0,domain[j])
    j = j + 1
j = 0
while j<1000:
    f1[j] = SHO(1,domain[j])
    j = j + 1
j = 0
while j<1000:
    f2[j] = SHO(2,domain[j])
    j = j + 1
j = 0
while j<1000:
    f3[j] = SHO(3,domain[j])
    j = j + 1
j = 0


plt.plot(domain,f0,label = 'Eigenstate n = 0')

plt.plot(domain,f1,label = 'Eigenstate n = 1')
plt.plot(domain,f2,label = 'Eigenstate n = 2')
plt.plot(domain,f3,label = 'Eigenstate n = 3')

plt.xlabel("Position X")
plt.ylabel("Wave function Shi")
plt.legend()
#plt.savefig('Q5.jpg')
plt.show()    
#Value of uncertainty in position for n=5 comes out to be 2.345 ~ 2.3
print("The value of uncertainty in position for x=5 is: ",np.sqrt(integral(5)))
 
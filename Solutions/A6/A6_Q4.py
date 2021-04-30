# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 12:58:32 2021

@author: Archi
"""

from gaussxw import gaussxw
import numpy as np
import matplotlib.pyplot as plt

def integrand(x):
    e = np.e
    f1 = e**x
    f1 = (f1 - 1)**-2
    f2 = x**4
    f2 = f2*e**x
    return f1*f2

def cv(T):
    x,w = gaussxw(50)
    V = 1
    rho = 6.022 * 10e28
    theta_D = 428
    
    a = 0
    b = theta_D/T
    
    xp = 0.5*(b-a)*x + 0.5*(b+a)
    wp = 0.5*(b-a)*w
    
    sum = 0
    i = 0
    while i<50:
        sum = sum + wp[i]*integrand(xp[i])
        i = i + 1
    Kb = 1.38065 * 10e-23
    sum = sum*9*rho*V*Kb*(T/theta_D)**3
    return sum

def plot():
    T = np.linspace(5,500,495)
    i = 0
    Cv = np.zeros(495)
    while i<495:
        Cv[i] = cv(T[i])
        i = i + 1
    plt.plot(T,Cv)
    plt.xlabel("Temperature")
    plt.ylabel("Heat Capacity of Solids")
    #plt.savefig('Q4.jpg')
    plt.show()

plot()

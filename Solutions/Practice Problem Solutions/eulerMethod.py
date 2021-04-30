import numpy as np
import matplotlib.pyplot as plt

"""
This is the Euler method to solve differential equations like:

dx/dt = f(x,t) where x(t) is the solution to this differential equation. t is the independant variable

Euler method is the First order Runge Kutta method
"""

def f(x,t):
    return -x**3 + np.sin(t) #Replace this with the function you want. What to do with singularities???

def solve(x_initial, t_initial, t_stop,dt):

    """
    x_intiial is the initial value of x at the time t_initial
    t_stop is to indicate the stop time of the iterations
    dt is the incremental time step

    """

    t_val = []
    x_val = []

    t_val.append(t_initial)
    x_val.append(x_initial)

    t = t_initial
    i = 0
    while t <= t_stop :
        x_val.append(x_val[i]+dt*f(x_val[i],t))

        t += dt
        t_val.append(t)
        i += 1

    return t_val,x_val

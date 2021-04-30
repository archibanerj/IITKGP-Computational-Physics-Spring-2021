import numpy as np
import matplotlib.pyplot as plt

def f(x,t):
    return -x**3 + np.sin(t) #Replace this with the function you want. What to do with singularities???


def solve(x_initial, t_initial, t_stop,dt):

    """
    x_intiial is the initial value of x at the time t_initial.
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
        k1 = dt*f(x_val[i],t)
        k2 = dt*f(x_val[i] + 0.5*k1,t + 0.5*dt)
        k3 = dt*f(x_val[i] + 0.5*k2,t + 0.5*dt)
        k4 = dt*f(x_val[i] + k3,t + dt)
        x_val.append(x_val[i]+ (1/6)*(k1 + 2*k2 + 2*k3 + k4))
        t += dt
        t_val.append(t)
        i += 1

    return t_val,x_val

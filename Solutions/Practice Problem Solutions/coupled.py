import matplotlib.pyplot as plt
import numpy as np

#See Vectorised implementation in odesim.py

def f(x,y,t):
    return x*y - x
def g(x,y,t):
    return y - x*y + np.sin(t)**2

def solve(x_initial, y_initial, t_initial, t_stop,dt):

    """
    (x_intiial,y_initial) is the initial value of (x,y) at the time t_initial.
    t_stop is to indicate the stop time of the iterations
    dt is the incremental time step
    """

    t_val = []
    x_val = []
    y_val = []

    t_val.append(t_initial)
    x_val.append(x_initial)
    y_val.append(y_initial)


    t = t_initial
    i = 0

    while t <= t_stop :
        k1 = dt*f(x_val[i],y_val[i],t)
        l1 = dt*g(x_val[i],y_val[i],t)
        k2 = dt*f(x_val[i] + 0.5*k1,y_val[i] + 0.5*l1,t + 0.5*dt)
        l2 = dt*g(x_val[i] + 0.5*k1,y_val[i] + 0.5*l1,t + 0.5*dt)
        k3 = dt*f(x_val[i] + 0.5*k2,y_val[i] + 0.5*l2,t + 0.5*dt)
        l3 = dt*g(x_val[i] + 0.5*k2,y_val[i] + 0.5*l2,t + 0.5*dt)
        k4 = dt*f(x_val[i] + k3,y_val[i] + l3,t + dt)
        l4 = dt*g(x_val[i] + k3,y_val[i] + l3,t + dt)

        x_val.append(x_val[i]+ (1/6)*(k1 + 2*k2 + 2*k3 + k4))
        y_val.append(y_val[i]+ (1/6)*(l1 + 2*l2 + 2*l3 + l4))

        t += dt
        t_val.append(t)
        i += 1

    return t_val,x_val,y_val

x_initial = 1
y_initial = 1
t_initial = 0
t_stop = 10
dt = 0.001

t,x,y = solve(x_initial, y_initial, t_initial, t_stop,dt)

#fig,P = plt.subplots(1,2)

"""
P[0].plot(t,x)
P[0].set_label("X")
P[1].plot(t,y)
P[1].set_label("Y")

fig.tight_layout()
"""

plt.plot(t,x)
plt.plot(t,y)

plt.show()

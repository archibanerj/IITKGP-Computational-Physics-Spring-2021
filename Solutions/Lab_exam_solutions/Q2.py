import matplotlib.pyplot as plt
import numpy as np

def f(r,t,g,l):
    theta = r[0]
    omega = r[1]

    f_theta = omega
    f_omega = -(g/l)*np.sin(theta)

    return np.array([f_theta,f_omega],float)

def solve(theta_initial, omega_initial, l, t_stop):
    g = 9.8

    dt = 0.01
    N = int(t_stop/dt)
    t = np.linspace(0,t_stop,N)

    theta = [theta_initial]
    r = [theta_initial , omega_initial]
    r = np.array(r,float)

    for i in range(1,N):
        k1 = dt*f(r,t,g,l)
        k2 = dt*f(r+0.5*k1,t+0.5*dt,g,l)
        k3 = dt*f(r+0.5*k2,t+0.5*dt,g,l)
        k4 = dt*f(r+k3,t+dt,g,l)
        r += (k1+2*k2+2*k3+k4)/6

        theta.append(r[0])

    plt.plot(t,theta)
    plt.ylabel("Angular Displacement")
    plt.xlabel("Time")
    plt.show()

theta_0 = float(input("Enter the starting angle of pendulum in degrees: "))
omega_0 = float(input("Enter initial angular velocity in degree per second: "))
l = float(input("Enter length of pendulum in metre: "))
endtime = float(input("Enter stopping time of the simulation: "))

theta_0 = (np.pi/180)*theta_0
omega_0 = (np.pi/180)*omega_0

solve(theta_0,omega_0,l,endtime)

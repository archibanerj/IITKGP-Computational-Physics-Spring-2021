import numpy as np
import matplotlib.pyplot as plt

def time_evolution(T,a,domain):
    dt = 1e-4 #Choose the time step wisely. Check notes. If its more than a certain value solution diverges
    t = 0
    D = 4.25e-6

    fig,p = plt.subplots(1,5)

    p[0].plot(domain,T)
    p[0].set_title("t = 0")

    temp = T.copy()
    while t<=0.01:
        t = t + dt
        for i in range(1,len(T)-1):
            temp[i] = T[i] + dt*(D/(a**2))*(T[i+1]+T[i-1]-2*T[i])
        T = temp.copy()
    p[1].plot(domain,T)
    p[1].set_title("t = 0.01")

    while t<=0.1:
        t = t + dt
        for i in range(1,len(T)-1):
            temp[i] = T[i] + dt*(D/(a**2))*(T[i+1]+T[i-1]-2*T[i])
        T = temp.copy()
    p[2].plot(domain,T)
    p[2].set_title("t = 0.1")

    while t<=0.4:
        t = t + dt
        for i in range(1,len(T)-1):
            temp[i] = T[i] + dt*(D/(a**2))*(T[i+1]+T[i-1]-2*T[i])
        T = temp.copy()
    p[3].plot(domain,T)
    p[3].set_title("t = 0.4")

    while t<=1:
        t = t + dt
        for i in range(1,len(T)-1):
            temp[i] = T[i] + dt*(D/(a**2))*(T[i+1]+T[i-1]-2*T[i])
        T = temp.copy()
    p[4].plot(domain,T)
    p[4].set_title("t = 1")

    fig.tight_layout()
    plt.show()

intervals = int(input("Enter number of intervals for discretising x axis: "))
grid = intervals + 1
temperature = np.ones(grid)
initial_temp_left = int(input("Enter initial temperature on the left end of x-axis (in Celcius): "))
initial_temp_right = int(input("Enter initial temperature on the right end of x-axis (in Celcius): "))
initial_temp_body = int(input("Enter temperature in the metal (in Celcius): "))
temperature = (initial_temp_body+273)*temperature #20+273
temperature[0] = initial_temp_left+273 #50+273
temperature[len(temperature) - 1] = initial_temp_right+273 #0+273
a = (1/100)/intervals #length in metres between discrete points
domain = np.linspace(0,1,grid)*(1/100)
#print(domain)
time_evolution(temperature,a,domain)

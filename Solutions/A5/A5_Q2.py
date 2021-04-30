import numpy as np
import matplotlib.pyplot as plt

raw_data = np.loadtxt('data.txt')

#storing x and y data
x = raw_data[:,0]
y = raw_data[:,1]

#creating the plot figure
fig, graphs = plt.subplots(1,2)

#plotting x and y raw_data
graphs[0].plot(x,y)
graphs[0].set_title('Given Data')

#setting up the infinitesimal dx:
dx = x[1] - x[0]

#declaring forward , backward and central difference variables
forward = np.zeros(x.size)
backward = np.zeros(x.size)
central = np.zeros(x.size)

#computing each of the derivatives:

for i in range(x.size) :
    if i == 0:
        backward[i] = (y[i+1] - y[i])/dx
    else :
        backward[i] = (y[i] - y[i-1])/dx
    if i == x.size-1:
        forward[i] = (y[i] - y[i-1])/dx
    else :
        forward[i] = (y[i+1] - y[i])/dx
    if (i>0)&(i<x.size-1) :
        central[i] = (y[i+1]-y[i-1])/(2*dx)

#plotting the variables
graphs[1].plot(x,forward,label = 'forward')
graphs[1].plot(x,backward,label = 'backward')
graphs[1].plot(x,central,label = 'central')
graphs[1].set_title('Calculated Derivative')
graphs[1].legend()
fig.tight_layout()
plt.savefig('Question 2 Plot')
plt.show()

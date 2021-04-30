# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:22:00 2021

@author: Archi
"""

import numpy as np
import matplotlib.pyplot as plt

x = y = np.linspace(-10,10,21)
X,Y = np.meshgrid(x,y)
u = X
v = Y
plt.rcParams["figure.figsize"] = (10,10) #sets the plot image dimensions
plt.quiver(X,Y,u,v)
theta = np.linspace(0,2*np.pi,100)
x1 = np.cos(theta)
y1 = np.sin(theta)
for i in range(1,10):
    plt.plot(i*x1,i*y1,'b')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

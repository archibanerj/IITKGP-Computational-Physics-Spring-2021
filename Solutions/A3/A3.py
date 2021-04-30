# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:46:07 2021

@author: Archi
"""

import numpy as np
import matplotlib.pyplot as plt

fig,A = plt.subplots(1,2)
theta1 = np.linspace(0,2*np.pi,100)
theta2 = np.linspace(0,10*np.pi,1000)
X1 = 2*np.cos(theta1) + np.cos(2*theta1)
Y1 = 2*np.sin(theta1) - np.sin(2*theta1)
X2 = (theta2**2)*np.cos(theta2)
Y2 = (theta2**2)*np.sin(theta2)
A[0].plot(X1,Y1)
A[0].set_xlabel('x axis')
A[0].set_ylabel('y axis')
A[1].plot(X2,Y2)
A[1].set_xlabel('x axis')
A[1].set_ylabel('y axis')
fig.tight_layout()
fig
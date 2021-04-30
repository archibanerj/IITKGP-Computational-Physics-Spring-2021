# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:06:02 2021

@author: Archi
"""

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0,2*np.pi,100)
X = 2*np.cos(theta) + np.cos(2*theta)
Y = 2*np.sin(theta) - np.sin(2*theta)

plt.plot(X,Y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Deltoid')
plt.show()
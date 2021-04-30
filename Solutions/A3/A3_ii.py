# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:36:54 2021

@author: Archi
"""

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0,10*np.pi,10000)
X = (theta**2)*np.cos(theta)
Y = (theta**2)*np.sin(theta)

plt.plot(X,Y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Spiral')
plt.show()

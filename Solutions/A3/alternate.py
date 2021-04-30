# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:04:41 2021

@author: Archi
"""

#This is a galilian spiral on a polar coordinate system!

import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection='polar')
theta = np.linspace(0,10*np.pi,1000)
ax.plot(theta,theta**2) #(theta,r)
plt.show()
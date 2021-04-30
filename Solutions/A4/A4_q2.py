# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:01:31 2021

@author: Archi
"""

import numpy as np

A = np.zeros([10,10])
for i in range(0,10):
    A[0,i] = 1
for i in range(1,10):
    A[i,9] = 1
for i in range(0,9):
    A[9,i] = 1
for i in range(0,10):
    A[i,0] = 1
print(A)
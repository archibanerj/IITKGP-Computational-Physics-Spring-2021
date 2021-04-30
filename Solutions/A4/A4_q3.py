# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:11:57 2021

@author: Archi
"""

import numpy as np

def func(n):
    A = np.zeros(3*n)
    for i in range(0,3*n):
        A[i] = i%3 + 1
    print(A)

N=-1
while N<=0:
    N = int(input("Enter the integer n: "))
    if N<=0:
        print("\nPlease give valid input\n")
func(N)
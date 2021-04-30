# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 01:11:02 2021

@author: Archi
"""
import numpy as np

#This code is written to multiply two matrices


def multiply(n):
    A = np.zeros([n,n],int) #the second argument sets the type of the array, which is 
    B = np.zeros([n,n],int) #float by default
    for i in range(n):
        for j in range(n):
            A[i,j] = (i+1)*(j+1)
            B[i,j] = i+j
    C = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i,j] += A[i,k]*B[k,j]
    print("A= \n",A)
    print("B= \n",B)
    print("C=A*B= \n",C)
    print("\nChecking using inbuilt function: \n",np.matmul(A,B))

multiply(int(input("Enter the size of square matrix ")))
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:15:47 2021

@author: Archi
"""

prec = 1 #variable holding the machine precision value upto a factor of 2
one = 0 
count = 0

while one !=1 :
    prec = prec/2
    one = 1 + prec
    count = count + 1
    

print("Number of loop executions: ",count)
print("Machine Precision within a factor of 2: ",prec)

import numpy as np

def func(x):
    return x**4 - 2*x + 1

domain = np.linspace(0,2,101)
f = func(domain)
h = 0.02
i = 1
sum = 0
while i<100 :
    sum  = sum + (h/3)*(f[i-1]+4*f[i]+f[i+1])
    i = i + 2

print("The integral is: ",sum)

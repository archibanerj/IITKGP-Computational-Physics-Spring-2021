import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return (x**4) - 2*x + 1

def integration(N):
    #defining the domain number of points
    """
    N = 11 #10 slices
    N = 101 #100 slices
    N = 1001 #1000 slices
    """
    """
    For N = 11 (10 slices) : Integral is 4.50656; Absolute Fractional Error is 0.024218
    For N = 101 (100 slices) : Integral is 4.40106; Absolute Fractional Error is 0.0002424218
    For N = 1001 (1000 Slices) : Integral is 4.4000106; Absolute Fractional Error is 2.424242*10^-6

    """
    domain = np.linspace(0,2,N)
    dx = domain[1] - domain[0]

    #setting the function
    f = func(domain)
    integral = 0

    #computing the integral numerically
    #Equation of Trapezoid rule: h*(sum of values of f excluding boundary points + 0.5*(f(a)+f(b))
    #sum of values of f excluding boundary points: sum of all f values - f(a) - f(b)
    return (np.sum(f) - (f[0]+f[N-1])/2)*dx

N = int(input("Enter number of points: "))
integral = integration(N)
print("The integral is: ",integral)
print("The absolute fractional error is: ", abs(1 - float(integral/4.4)))

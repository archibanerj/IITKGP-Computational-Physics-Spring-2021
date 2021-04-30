import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.sin(x) + 2*np.cos(x)

def interpolate(x,samples,values) :
    #x - domain point at which we have to find the value of the interpolated polynomial
    #samples - the points at which the values of original function have been sampled
    #values - values of the original function for each sample

    N = len(samples)
    i = 0
    j = 0
    term = 0
    sum = 0
    while i<N :
        term = 1
        while j<N:
            if i!=j:
                term = term * (x-samples[j]) / (samples[i] - samples[j])
            j += 1
        j = 0
        sum = sum + term*values[i]
        i += 1
    return sum

#In this section, we will print the interpolated value for a given sample point between 0 and pi

domain = np.linspace(0,np.pi,10)
f = func(domain)

x = float(input("Enter test value of x between 0 and pi to check correctness: "))
print("Value obtained from original function: ",func(x))
print("Value obtained from interpolated polynomial: ",interpolate(x,domain,f))

#Value obtained at x = 2.1 : -0.146 (to 3 decimal places)

"""
Now we shall plot this function with 30 sample points

In this section, we use 10 evenly spaced points of the 'domain' array above
along with the 'f' values for each point, to construct the interpolation function.

We find out the values of the interpolation function
for 30 evenly spaced points, and plot them over
the graph for values obtained from the given function sin x + 2*cos x
for the same 30 evenly spaced points

"""


N = 30
X_values = np.linspace(0,np.pi,N)
Y = np.zeros(N)

i = 0
for i in range(N):
    Y[i] = interpolate(X_values[i],domain,f)

f = func(X_values)

plt.plot(X_values, Y, label = 'Interpolated Polynomial')
plt.plot(X_values, f, label = 'Given function')
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
plt.savefig('Q1.jpg')
plt.show()

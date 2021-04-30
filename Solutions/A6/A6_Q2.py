import numpy as np
import matplotlib.pyplot as plt


"""
Expected Value of T = 3.14 s

"""

A = int(input("Enter Amplitude: "))

def func(x):
    k = 4
    E = 0.5*k*A**2
    return np.sqrt(2/(E - 0.5*k*(x**2)))

def integrate(epsilon):
    domain = np.linspace(0,A-epsilon,101)
    f = func(domain)

    h = domain[1] - domain[0]
    i = 1
    sum = 0

    while i<100 :
        sum  = sum + (h/3)*(f[i-1]+4*f[i]+f[i+1])
        i = i + 2

    return sum*2

eps = np.linspace(0.001,0.01,101)
T = np.zeros(101)
i = 0

while i<101:
    T[i] = integrate(eps[i])
    i = i + 1

exp_T = (np.pi)*np.ones(101)
min = np.argmin(np.abs(T-exp_T))
best_eps = eps[min]
arr = best_eps*np.ones(len(T))
print("The best epsilon is: ",best_eps) #For Amplitude = 5, Best epsilon is: 0.00307
print("The Calculated integral for this epsilon is: ",T[min])

plt.figure(0)
plt.plot(np.log(eps),np.log(T),label = "Calculated T v/s epsilon")
plt.plot(np.log(eps),np.log(exp_T), label = "Expected T")
plt.plot(np.log(arr),np.log(T), label = "Best epsilon")
plt.legend()
plt.xlabel("Epsilon")
plt.ylabel("Calculated Time Period")
plt.title("Log-Log plot of T v/s epsilon")
plt.savefig("Q2.jpg")
plt.show()


"""
Ideally, the Time period v/s Amplitude curve should come out to be a 
line of zero slope. But in this case, unless we choose the proper epsilon,
we will not get that result. But fixing the epsilon is in a way comparing the
true value of the integral to the calculated value - this would mean
that we are fixing the integral value beforehand and printing it. Here, in
addition to the T v/s A curve, we also print the epsilon v/s A curve for correct T ~ 3.14s



Here, we calculate, for each Amplitude in the range 1 to 100,
the time period for each epsilon from 0.00001 to 0.1 in 1000 steps

We single out those T and those epsilon for which the T is closest to 
3.14 for each A. Then we make a plot of these T v/s  A, and then a 
plot for the optimal epsilon v/s each A

"""
A_values = np.linspace(1,100,100)
epsilon = np.zeros(100)
trial_eps = np.linspace(0.00001,0.1,1000)
temp_T = np.zeros(1000)
T = np.zeros(100)
i = 0
j = 0

while i<100:
    A = A_values[i]
    while j<1000:
        temp_T[j] = integrate(trial_eps[j])
        j = j + 1
    epsilon[i] = trial_eps[np.argmin(np.abs(temp_T-np.pi))]
    T[i] = temp_T[np.argmin(np.abs(temp_T-np.pi))]
    temp_T = np.zeros(1000)
    j = 0
    i = i + 1

plt.figure(1)
plt.plot(A_values,T)
plt.ylabel("Calculated T")
plt.xlabel("Amplitude")
plt.title("Time period T v/s amplitude A")
plt.savefig("TvsA_Q2.jpg")
plt.show() #In this plot, we observe a zig-zag line which oscillates
#Quite near the true value of time period, T = 3.14


plt.figure(2)
plt.plot(A_values,epsilon)
plt.ylabel("Calculated epsilon for near-correct T")
plt.xlabel("Amplitude")
plt.title("Optimal epsilon v/s amplitude A")
plt.savefig("EpsVSA_Q2.jpg")
plt.show()


"""
## An upgraded version of the same code:
# Slope of straight line plot: 0.000613885

slope = 0.000613885
eps = slope*A
Time_period = integrate(eps)
print(Time_period)

"""
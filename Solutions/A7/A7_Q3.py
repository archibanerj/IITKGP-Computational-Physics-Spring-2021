import numpy as np
import matplotlib.pyplot as plt
import cubicspline as cs

"""
We use cubic spline interpolation as it gives a
better estimate for x=pi/2 for both half data set
and the full one, as well as gives a good fit in the plot
"""

A = np.loadtxt('file_1.txt')
x = A[:,0]
y = A[:,1]

#Finding value at x = pi/2 using cubic spline Interpolation

print("Value at x = pi/2: ", cs.interpolate(np.pi/2,x,y,cs.double_primes(x,y)))
# With the given 259 points, we get answer as 0.9999

"""
Now we shall do this calculation with
the first half of the data set, that is with 130 points

"""

half_x = list(x)
half_y = list(y)
for i in range(129):
    half_x.pop()
    half_y.pop()

half_x = np.array(half_x)
half_y = np.array(half_y)


print("Value at x = pi/2 with half the points: ", cs.interpolate(np.pi/2,half_x,half_y,cs.double_primes(half_x,half_y)))
# Now with half the points the answer comes out as: 0.9999


#Visualising: We will now plot the half data set and the interpolation

N=100
domain = np.linspace(x[0],x[len(x)-1],N)
half_domain = np.linspace(half_x[0],half_x[len(half_x)-1],N)

f = np.zeros(N)
half_f = np.zeros(N)

for i in range(len(domain)):
    f[i] = cs.interpolate(domain[i],x,y,cs.double_primes(x,y))
    half_f[i] = cs.interpolate(half_domain[i],half_x,half_y,cs.double_primes(half_x,half_y))


fig, plots = plt.subplots(1,3)
plots[0].scatter(x,y,label = 'Given data')
plots[0].set_xlabel('X')
plots[0].set_ylabel('Y')
plots[0].set_title("Given data")
plots[1].plot(domain,f,label = 'Cubic Spline Interpolation')
plots[1].set_xlabel('X')
plots[1].set_ylabel('Y')
plots[1].set_title("Cubic Spline Interpolation")
plots[2].plot(half_domain,half_f,label = 'Cubic Spline Interpolation on half data set')
plots[2].set_xlabel('X')
plots[2].set_ylabel('Y')
plots[2].set_title("Cubic Spline Interpolation on half data set")
fig.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

"""
The n=2,3,4 graphs don't come out correctly
Only the n=1 graph comes out correctly
"""

def jacobi(n):
    #Initialising the domain
    intervals = 500
    dx = 1/intervals
    N = intervals + 1
    x_axis = np.linspace(0,1,N)

    shi = np.sin(x_axis)  #Initial guess for shi. We don't use shi = 0 as that will lead to a trivial solution.
    shi[0] = 0
    shi[N-1] = 0
    shi = shi/np.sqrt(np.trapz(shi**2,x_axis)) #Normalising initial wave function


    converge = False
    epsilon = 1e-6
    temp = np.zeros(N)

    w=0.9 #w for over-relaxation
    div = int(500/n)

    while not(converge):
        temp = shi.copy()
        for i in range(1,N-1):
            updated_shi = (shi[i-1]+shi[i+1])/(2 - (n*np.pi*dx)**2)
            shi[i] = (1+w)*updated_shi - w*shi[i] #Applying Gauss Siedel with Over-Relaxation

        shi = shi/np.sqrt(np.trapz(shi**2,x_axis))

        if max(abs(temp-shi))<epsilon: #Checking Convergence
            converge = True
        #print(max(abs(temp-shi)))



    return shi, x_axis



shi1,x_axis = jacobi(1)
shi2,x_axis = jacobi(2)
shi3,x_axis = jacobi(3)
shi4,x_axis = jacobi(4)

prob_density1= shi1**2
prob_density2= shi2**2
prob_density3= shi3**2
prob_density4= shi4**2

fig, P = plt.subplots(1,4)

P[0].plot(x_axis,prob_density1)
P[0].set_title("n=1")
P[0].set_xlabel("x axis")
P[0].set_ylabel("Probability Density")
P[1].plot(x_axis,prob_density2)
P[1].set_title("n=2")
P[1].set_xlabel("x axis")
P[1].set_ylabel("Probability Density")
P[2].plot(x_axis,prob_density3)
P[2].set_title("n=3")
P[2].set_xlabel("x axis")
P[2].set_ylabel("Probability Density")
P[3].plot(x_axis,prob_density4)
P[3].set_title("n=4")
P[3].set_xlabel("x axis")
P[3].set_ylabel("Probability Density")


fig.tight_layout()
plt.show()

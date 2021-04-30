import numpy as np

def func(x):
    return x**4 - 2*x + 1

def trapezoidal(domain,f):
    h = domain[1] - domain[0]
    return h*(2*np.sum(f) - f[0] - f[len(f)-1])/2

def euler_maclaurin(domain,f):
    h = domain[1] - domain[0]
    term_1 = trapezoidal(domain,f)
    dx = 1e-5
    a = domain[0]
    b = domain[len(domain)-1]

    f_prime_a = (func(a+dx/2)-func(a-dx/2))/(dx)
    f_prime_b = (func(b+dx/2)-func(b-dx/2))/(dx)

    term_2 = (1/12)*(f_prime_a - f_prime_b)*h**2
    return term_1 + term_2

X = np.linspace(0,2,10)
Y = func(X)

trap = trapezoidal(X,Y)
eul  = euler_maclaurin(X,Y)

print("The correct value of this integral is: ",4.4)
print("Output from trapezoidal rule: ", trap)
print("Error in result from trapezoidal rule: ", np.abs((trap-4.4)/4.4))
print("Output from Euler-Maclaurin rule: ", eul)
print("Error in result from Euler-Maclaurin rule: ", np.abs((eul-4.4)/4.4))
print("Thus, Euler Maclaurin method is more accurate")

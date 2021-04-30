
def func(x):
    return x**3 - x**2 + 2

def func_prime(x):
    return 3*x**2 - 2*x


counter = 0

def bisection(l,u):
    """
    Number of Iterations in this
    Implementation of Bisection Method: 56
    
    """
    global counter
    counter = counter + 1
    if func(l)==0 :
        print("Root obtained from Bisection: ",l)
    elif func(l)*func(u) < 0:
        if func((l+u)/2)*func(u) < 0:
            bisection((l+u)/2, u)
        else :
            bisection(l, (l+u)/2)

def NewRaph(x): 
    """
    Number of iterations in this implementation of
    Newton Raphson Method: 7 
    
    This is considerably less than Bisection Method
    
    Initial Guess: -0.5
    """
    global counter
    counter  = counter + 1
    if func(x) == 0:
        print("Root Obtained from Newton Raphson: ",x)
    else :
        x_1 = x - (func(x)/func_prime(x))
        NewRaph(x_1)
    
NewRaph(-0.5)
print("Initial Guess for Newton Raphson: -0.5")
print("Iterations for Newton Raphson: ",counter)
counter = 0
bisection(-5,5)
print("Initial guess interval for Bisection: [-5,5]")
print("Iterations for Bisection: ",counter)

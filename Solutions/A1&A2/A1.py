N = int(input("Which fibonacci term?\n"))

def fibonacci(n) : #solution with loop
    i = 1;
    a = c = 0;
    b=0;
    for j in range(1,n) :
        b=a;
        a=i
        i=i+c
        c=a
    print("Term: ",a)
    print("Ratio: ", '%.3f'%(a/b))

print('This is a non- recursive solution\n')
fibonacci(N)

print('\nThis is the recursive solution\n')

def fib(i): #recursive function call
    if i==1:
        return 0
    elif i==2:
        return 1
    else:
        return fib(i-1) + fib(i-2)

print("Term: ",fib(N))

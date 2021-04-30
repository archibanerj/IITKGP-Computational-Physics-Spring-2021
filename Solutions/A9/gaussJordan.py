import numpy as np

def solve(A,b):
    n = len(A)
    C = np.append(A,b,axis = 1)
    for i in range(n-1):
        C[i] = C[i]/C[i][i]
        for j in range(i+1,n):
            C[j] = C[j] - C[i]*C[j][i]


    if C[n-1][n-1]<0: #Correct this step if necessary
        C[n-1] = C[n-1]*-1

    i = n-1
    while i > 0:
        j = i-1
        while j >= 0:
            C[j] = C[j] - C[i]*C[j][i]
            j -= 1
        i -= 1

    A = C[:,0:n]
    b = C[:,n:n+1]

    return A,b

def pivot_solve(A,b):
    n = len(A)
    C = np.append(A,b,axis = 1)

    for i in range(n-1):
        if C[i][i] == 0:
            for k in range(n): #Swapping with a row having a non-zero pivot element - if this method fails to swap, then the system is singular
                if C[k][i] != 0:
                    temp = C[k].copy()
                    C[k] = C[i].copy()
                    C[i] = temp.copy()

        C[i] = C[i]/C[i][i]
        for j in range(i+1,n):
            C[j] = C[j] - C[i]*C[j][i]

    if C[n-1][n-1] != 1:
        C[n-1] = C[n-1]/C[n-1][n-1]

    i = n-1
    while i > 0:
        j = i-1
        while j >= 0:
            C[j] = C[j] - C[i]*C[j][i]
            j -= 1
        i -= 1

    A = C[:,0:n]
    b = C[:,n:n+1]

    return A,b

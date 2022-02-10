import numpy as np
def linearsolver(A,b):
    n = len(A)
    M = A
    U=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    i = 0
    for x in M:
        x.append(b[i])
        i += 1

    for k in range(n):        
        for i in range(k+1,n):
            q = -M[i][k] / M[k][k]
            for j in range(k, n+1):
                M[i][j] +=  q * M[k][j]
                U[i][k] = -q                    

    x = [0 for i in range(n)]

    for row in M:        
        x[n-1] =float(M[n-1][n])/M[n-1][n-1]
        for i in range (n-1,-1,-1):
            z = 0
            for j in range(i+1,n):
                z = z  + float(M[i][j])*x[j]
            x[i] = float(M[i][n] - z)/M[i][i]        
    print(x)
    print("matriz triangular superior: "+str(M))
    print("matriz triangular inferior: "+str(U))
    #se multiplica U*M
# A = [[2,1,3], [2, 6, 8], [6,8,18]]
# b = [1,3,5]
# linearsolver(A,b)  

A = [[6,-2,2,4],[12,-8,6,10],[3,-13,9,3],[-6,4,1,-18]]
b = [16,26,-19,-34]
linearsolver(A,b)  

# A = [[0,2,0,1], [2,2,3,2], [4,-3,0,1], [6,1,-6,-5]]
# b = [0,-2,-7,6]
# linearsolver(A,b)  
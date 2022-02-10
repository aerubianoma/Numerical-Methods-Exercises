
def linearsolver(A,b):
    n = len(A)
    M = A

    i = 0
    for x in M:
        x.append(b[i])
        i += 1
    for k in range(n):  
        if M[k][k]==0:
            for l in range(n):
                if M[k][k]!=0:
                    break
                if M[k][k]<abs(M[k+l+1][k]):
                    c=M[k]
                    M[k]=M[k+l+1]
                    M[k+l+1]=c
                    if M[k][k]!=0:
                        for i in range(k+1,n):
                            q = -M[i][k] / M[k][k]
                            for j in range(k, n+1):
                                M[i][j] +=  q * M[k][j]
                
        else:
            for i in range(k+1,n):
                q = -M[i][k] / M[k][k]
                for j in range(k, n+1):
                    M[i][j] +=  q * M[k][j]                
    x = [0 for i in range(n)]

    for row in M:        
        x[n-1] =float(M[n-1][n])/M[n-1][n-1]
        for i in range (n-1,-1,-1):
            z = 0
            for j in range(i+1,n):
                z = z  + float(M[i][j])*x[j]
            x[i] = float(M[i][n] - z)/M[i][i]   
    print("la matriz resultante es:")
    print(x)

# A = [[2,1,3], [2, 6, 8], [6,8,18]]
# b = [1,3,5]
# linearsolver(A,b)  

#A = [[6,-2,2,4],[12,-8,6,10],[3,-13,9,3],[-6,4,1,-18]]
#b = [16,26,-19,-34]
#linearsolver(A,b)  

A = [[0,2,0,1], [2,2,3,2], [4,-3,0,1], [6,1,-6,-5]]
b = [0,-2,-7,6]
linearsolver(A,b)


# In[ ]:




# In[ ]:




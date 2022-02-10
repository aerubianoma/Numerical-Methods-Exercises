A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,0,0],[0,1,0],[0,0,1]]
#verificar si la multiplicacion esta definida
if len(A[0])==len(B):
    print("la multiplicacion de matrices es posible")
else:
    print("la suma de matrices no es posible")
print("--------------------------------------------")
M=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(B[i])):
        for k in range(len(B)):
            M[i][j]+=(A[i][k]*B[k][j])
print(M)
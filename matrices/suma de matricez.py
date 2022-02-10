A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,3],[4,5,6],[7,8,9]]
#verificacion de tamaño de matrices
c=0
if len(A)==len(B):
    for i in range(len(A)):
        if len(A[i])==len(B[i]):
            c+=1
            if c==3:
                print("se puede efectar la suma entre las dos matrices")
        else:
            print("la suma no se puede efectuar")
else:
    print("no se puede efectuar la suma entre las dos matices")
#suma de matrices
S=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(A[i])):
        S[i][j]=(A[i][j]+B[i][j])
print(S)
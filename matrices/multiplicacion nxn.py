v1=[] 
v3=[]  
v5=[] 
print("ingrese tamaño de la primera matriz")
n,m=int(input()),int(input()) 
print("ingrese tamaño de la segunda matriz")
j,k=int(input()),int(input()) 

if m!=j:
  print("Matrices no válidas para multiplicacion")
if m==j:
  for i in range(n):
    v2=[]
    for l in range(m):
        print("ingrese el valor de : "+"("+str(i)+","+str(l)+")")    
        v2.append(float(input()))
    v1.append(v2)
  for i in range(j):
    v4=[]
    for l in range(k):
        print("ingrese el valor de : "+"("+str(i)+","+str(l)+")") 
        v4.append(float(input()))
    v3.append(v4)
for i in range(n):
    v6=[] 
    for l in range(k):
      v6.append(0)
    v5.append(v6)
for i in range(len(v1)):
    for l in range(len(v3[i])):
        for m in range(len(v3)):
            v5[i][l]+=v1[i][m]*v3[m][l]
print("la nueva matriz es:")
for t in range(len(v5)):
    print(v5[t])


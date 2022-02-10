v1=[] 
v3=[]  
v5=[]
v7=[]
n=int(input()) 
m=int(input()) 
j=int(input()) 
k=int(input()) 
if m!=j:
  print("Matrices no válidas")
if m==j==k:
  for i in range(n):
    v2=[]
    for l in range(m):
      v2.append(float(input()))
    v1.append(v2)
  for i in range(j):
    v4=[]
    for l in range(k):
      v4.append(float(input()))
    v3.append(v4)
  for i in range(k):
    v8=[]
    for l in range(j):
      v8.append(v3[l][i])
    v7.append(v8)
  for i in range(n):
    v6=[] 
    for l in range(j):
      v6.append(0)
    v5.append(v6)
  for i in range(len(v1)):
    for l in range(len(v7[i])):
        for m in range(len(v7)):
            v5[i][l]+=v1[i][m]*v7[m][l]
  print(v5)
n=int(input())
c=0
b=0
suma=0
a=((n*(n+1)*((2*n)+1))/6)
print(a)
while c<=n:
    b=c**2
    suma+=b
    c+=1
print(suma)

 
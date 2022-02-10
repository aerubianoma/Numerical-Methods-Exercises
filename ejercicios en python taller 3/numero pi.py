print("ingrese un valor para n:")
n=float(input())
i=float(2)
c=float(4)
while i<=n:
    if i%2==0:
        c=c-(4/((2*i)-1))
        i=i+1
       
    else:
        c=c+(4/((2*i)-1))
        i=i+1
       
        
print(float(c))
        

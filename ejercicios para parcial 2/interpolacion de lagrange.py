n=int(input("Numero de puntos: "))
va=[];
vb=[];
x=float(input("Valor a aproximar: "))
for j in range(n):
    a=float(input("valor x"+str(j)+": "))
    va.append(a)
    b=float(input("valor f(x"+str(j)+"): "))
    vb.append(b)
def f(x):
    return ((x-xi)/(xk-xi));
l=0;
vo=[]
while l<n:
    m=0;
    o=1;
    while m<n:
        xk=va[l]
        xi=va[m]
        if (xk-xi==0):
            m+=1;
        else:
            m+=1;
            o*=f(x);
    vo.append(o)
    l+=1;
r=0;
for i in range(n):
    r+=(vb[i]*vo[i]);
print("El valor de "+str(x)+" en f(x) es: "+str(r))

   
   



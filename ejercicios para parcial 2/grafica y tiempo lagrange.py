import time
import random
t1=time.time()
n=int(1000)
va=[];
vb=[];
x=float(random.randrange(1,1000))
for k in range(n):
    a=float(k)
    va.append(a)
for j in range(n):
    b=float(random.randrange(1,1000))
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
t2=time.time()
t=t2-t1
print(t)

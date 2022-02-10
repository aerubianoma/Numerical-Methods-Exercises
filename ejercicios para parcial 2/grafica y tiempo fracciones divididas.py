import time
import random
t1=time.time()
n=int(1000)
vx=[]
vy=[]
vo=[]
vp=[]
o=1;
y=int(100)
for k in range(n):
    a=float(k)
    vx.append(a)
for j in range(n):    
    b=int(random.randrange(1000,2000))
    vy.append(b)
px=vy[0]
def f(x):
        return (x-x0);
def g(x):
    return ((vy[x+1]-vy[x])/(vx[x+u]-vx[x]))   
u=1;
for k in range(n-1):
    x0=vx[k]
    o*=f(y);
    vo.append(o)
    vz=[]
    for t in range(n-u):
        p=g(t);
        vz.append(p)
    u+=1;
    vy=vz;
    vp.append(vy[0])
for r in range(n-1):
   px+=(vp[r]*vo[r]);
   print(px)
print("valor de la funcion en "+str(y)+" "+str(px))
t2=time.time()
print(t2-t1)

n=int(input("Número de puntos= "))
vx=[]
vy=[]
vo=[]
vp=[]
o=1;
y=float(input("Valor a aproximar= "))
for j in range(n):
    a=float(input("valor x"+str(j)+"= "))
    vx.append(a)
    b=float(input("valor f(x"+str(j)+")= "))
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
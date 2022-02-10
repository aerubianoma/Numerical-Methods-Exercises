import math
def f(x):
    return (x**2)-5
a=0
b=5
e=0
error=[]
c=1
while c<=20:
    m=((f(a)-f(b))/(a-b))
    x=a-(f(a)/m)    
    e=f(x)
    if e>0:
        b=x
        e=f(b)
        print("el valor de la raiz en la iteracion N° "+str(c)+": "+str(x))
    elif e<0:
        a=x
        e=f(a)
        print("el valor de la raiz en la iteracion N° "+str(c)+": "+str(x))
    error.append(abs(x-math.sqrt(5)))
    c+=1
    if (abs(f(x)))<(1*(10**-4)):
        break
print("numero de iteraciones: "+str(c-1))
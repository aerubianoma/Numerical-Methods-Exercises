import math
def f(x):
    return (x**2)-5
def g(x):
    return (2*x)
a=1
error=[]
c=1
while c<=20:
    x=a-(f(a)/g(a))
    a=x
    print("valor aproximado en la iteracion N° "+str(c)+": "+str(a))
    error.append(a)
    if (abs(f(a)))<(1*(10**-4)):
        break;
    c+=1    
print("numero de iteraciones: "+str(c))
print(error)
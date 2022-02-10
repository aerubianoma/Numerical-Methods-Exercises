import math
def f(x):
    return math.cos(x)-(x**3)
def g(x):
    return (-1*math.sin(x))-(3*(x**2))
a=1
c=1
while c<=20:
    x=a-(f(a)/g(a))
    a=x
    print("valor aproximado en la iteracion N° "+str(c)+": "+str(a))
    if (abs(f(a)))<(1*(10**-4)):
        break;
    c+=1    
print("numero de iteraciones: "+str(c))

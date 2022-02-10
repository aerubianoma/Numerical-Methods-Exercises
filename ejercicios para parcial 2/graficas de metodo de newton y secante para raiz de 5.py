print("-----------------------------------------------------------------------------")
print("Metodo de Newton:")
import matplotlib.pyplot
import numpy
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
    print("valor aproximado en la iteracion N° "+str(c-1)+": "+str(a))
    error.append(a)
    if (abs(f(a)))<(1*(10**-4)):
        break;
    c+=1    
print("numero de iteraciones: "+str(c-1))
print("error en cada iteracion: "+str(error))
print("-----------------------------------------------------------------------------")
print("Metodo de la secante:")
import math
def f(x):
    return (x**2)-5
a=0
b=5
e=0
error2=[]
c=1
while c<=20:
    m=((f(a)-f(b))/(a-b))
    x=a-(f(a)/m)    
    e=f(x)
    if e>0:
        b=x
        e=f(b)
        print("el valor de la raiz en la iteracion N° "+str(c-1)+": "+str(x))
    elif e<0:
        a=x
        e=f(a)
        print("el valor de la raiz en la iteracion N° "+str(c-1)+": "+str(x))
    error2.append(abs(x-math.sqrt(5)))
    c+=1
    if (abs(f(x)))<(1*(10**-4)):
        break
print("numero de iteraciones: "+str(c-2))
print("error en cada iteracion :"+str(error2))
print("----------------------------------------------------------------------------")
print("Grafica:")
import matplotlib.pyplot as plt
import numpy as np
plt.plot(error)
plt.plot(error2)
plt.title("Grafica error vs iteracion")   # Establece el título del gráfico
plt.xlabel("iteracion")   # Establece el título del eje x 
plt.ylabel("error")   # Establece el título del eje y
plt.plot(error, label = "Metodo de Newton")
plt.plot(error2, label = "Metodo de la secante")
plt.legend()
plt.show()
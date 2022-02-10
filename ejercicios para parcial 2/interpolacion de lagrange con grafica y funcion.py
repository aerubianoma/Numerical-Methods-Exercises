import scipy
import matplotlib.pyplot as plt
import numpy as np
x =scipy.array([0,0.5,1,1.5,2])
y =scipy.array([0,0.19,0.26,0.29,0.1])
resultado = scipy.poly1d([0.0])
for i in range(0,len(x)):
    numerador = scipy.poly1d([1.0])
    denominador = 1.0
    for j in range(0,len(x)):
        if i != j:
            numerador *= scipy.poly1d([1.0,-x[j]])
            denominador *= x[i]-x[j]
    resultado += (numerador/denominador)*y[i]
print("el resultado es: ")
print(resultado)
print("----------------------------------------------------------------------")
n=float(input("digite un valor para x y evaluarlo en la funcion:"))
print("la funcion evaluada en el punto ingresado es: "+str(resultado(n)))
x_val = np.arange(min(x),max(x)+1, 0.1)
plt.xlabel("x") ; plt.ylabel("p(x)")
plt.grid(True)
for i in range (0,len(x)):
    plt.plot(x[i],y[i],)
plt.plot(x_val,resultado(x_val))
plt.axis([min(x)-1,max(x)+1,min(y)-1,max(y)+1])
plt.show()

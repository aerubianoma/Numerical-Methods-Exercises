import math
def f(x):
    return ((math.sin((math.sqrt(x**2+x))/(math.cos(x)-x)))**2)/(math.sin((math.sqrt(x)-1)/(math.sqrt(x**2+1))))
h=1*10**-4
x=0.25
a=x-h
b=x
c=x+h
d=x+2*h
db=(f(b)-f(a))/(h)
df=(f(c)-f(b))/(h)
dc=(f(c)-f(a))/(2*h)
z=(-3*f(b)+4*f(c)-f(d))/(2*h)
w=((f(d)-2*f(c)+f(x))/h**2)
print(str(df)+" = derivacion hacia adelante")
print(str(db)+" = derivacion hacia atras")
print(str(dc)+" = derivacion centrada")
print(str(z)+" = derivacion por lagrange")
print(str(w)+" = segunda derivada")

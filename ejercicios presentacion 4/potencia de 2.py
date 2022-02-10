print("ingrese un numero para saber si es potencia de 2")
n=int(input())
a=n&n-1
if n==0:
    print("el numero ingresado no es potencia de 2")
elif a==0:
    print("el numero ingresado  es potencia de 2")
else:
    print("el numero ingresado no es potencia de 2")
    
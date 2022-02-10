print("ingrese un numero para saber si es primo")
numero=int(input())
if numero==2 or numero==3 or numero==5:
    print("el numero ingresado es primo")
elif numero==1 or numero%2==0 or numero%3==0 or numero%5==0:
    print("el numero ingresado no es primo")
else:
    print("el numero es primo")

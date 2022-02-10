print("ingrese un valor para n y conocer la serie de fibonacci hasta ese numero")
n=int(input())
contador=0
primero=1
segundo=0
ultimo=0
print("-------------------------------------")
while contador<=n:
    ultimo=primero+segundo
    print(ultimo)
    primero=segundo
    segundo=ultimo
    contador+=1

numero=int(input())
contador=1
suma=0
while contador<=(numero-1):
    if numero%contador==0:
        suma+=contador
    contador+=1
if suma>numero:
    print("el numero es abundante")
else:
    print("el numero no es abundante")
    
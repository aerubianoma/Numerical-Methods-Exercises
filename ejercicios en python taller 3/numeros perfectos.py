print("ingrese un numero para saber si es perfecto")
numero=int(input())
contador=1
suma=0
while contador<=numero-1:
    if numero%contador==0:
        suma=suma+contador
    contador+=1        
if suma==numero:
    print("el numero ingresado es perfecto")
else:
    print("el numero ingresado no es perfecto")
        
    
    
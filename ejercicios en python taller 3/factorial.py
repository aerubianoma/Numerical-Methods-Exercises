print("ingrese un valor para obtener su factorial")
numero=int(input())
contador=1
valor=1
print("----------------------------------")
while contador<=numero:
    valor=valor*contador
    contador+=1
print(str(numero)+"! = "+str(valor))

    
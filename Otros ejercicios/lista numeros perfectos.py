print("ingrese un numero para conocer la lista de numeros perfectos desde 0 hasta ese numero")
numi=int(input())
print("----------------------------------------------------------------------")
print("la lista de numeros perfectos desde 0 hasta "+str(numi)+" es:")
numero=1
while numero<=numi:
    contador=1
    suma=0
    while contador<=(numero-1):
        if numero%contador==0:
            suma+=contador
        contador+=1
    if suma==numero:
        print(numero)
    numero+=1
    
print("ingrese un numero para conocer la lista de numeros abundantes desde 0 hasta el numero ingresado")
numi=int(input())
print("----------------------------------------------------------------------")
print("la lista de numeros abundantes que hay desde 1 hasta "+str(numi)+" es:")
numero=1
while numero<=numi:
    contador=1
    suma=0
    while contador<=(numero-1):
        if numero%contador==0:
            suma+=contador
        contador+=1
    if suma>numero:
        print(numero)
    numero+=1
if numi<12:
    print("no existen numeros abundantes desde 0 hasta 11")
    
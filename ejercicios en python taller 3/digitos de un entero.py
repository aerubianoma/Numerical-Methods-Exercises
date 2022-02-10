print("ingrese un numero para saber cuantos digitos tiene")
n=int(input())
contador=1
while n>=10:
    n=n/10
    contador+=1
print("tiene "+str(contador)+" digito(s)")


print("ingrese un numero para saber su tabla de multiplicar del 0 al 10:")
n=int(input())
c=0
m=0
print("-----------------------------")
while c<=10:
    m=n*c
    print(str(n)+"*"+str(c)+"="+str(m))
    c+=1

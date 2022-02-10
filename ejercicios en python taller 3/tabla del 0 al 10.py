print("Tabla de multiplicar del 0 al 10:")
n=0
tabla=0
m=0
print("-----------------------------")
while tabla<=10:
    multiplicacion=0
    print("tabla del "+str(tabla)+":")
    while multiplicacion<=10:
        n=multiplicacion*tabla           
        print(str(tabla)+"*"+str(multiplicacion)+"="+str(n))
        multiplicacion+=1
    tabla+=1
        
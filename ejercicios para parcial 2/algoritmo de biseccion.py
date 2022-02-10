a=0.5
b=15
c=0
n=0
while n<=10:
    if ((a**2)-1)<0 and ((b**2)-1)>0:
        print("iteracion N°"+str(n)+": "+"el cero se encuentra en el intervalo ("+str(a)+","+str(b)+")")
        c=(a+b)/2        
        b=c        
    elif ((a**2)-1)>0 and ((b**2)-1)<0:
        print("iteracion N°"+str(n)+": "+"el cero se encuentra en el intervalo ("+str(a)+","+str(b)+")")
        c=(a+b)/2        
        b=c        
    else: 
        print("iteracion N°"+str(n)+": "+"el cero no se encuentra en ese intervalo ("+str(a)+","+str(b)+")")
        print("-------------------------------------------------------------------------------")
        break    
    n+=1
print("se necesitaron "+str(n)+" iteraciones para econtrar el intervalo mas pequeño")    
        


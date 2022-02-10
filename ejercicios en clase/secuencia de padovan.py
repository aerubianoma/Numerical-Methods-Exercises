n=int(input())
p0=1
p1=1
p2=1
c=1
print("----------------------------------------------------")
print("la secuencia de padovan hasta "+"n="+str(n))
print(p0)
print(p1)
print(p2)  
while c<=n:         
    pn=p1+p0
    print(pn)
    p0=p1
    p1=p2
    p2=pn    
    c+=1
    
    
    

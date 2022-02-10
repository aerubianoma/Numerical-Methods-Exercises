x=int(input())
y=int(input())
z=int(input())
if x<y and y<z:
    print(str(x)+" es menor que "+str(y)+" y "+str(y)+" es menor que "+str(z))
elif z<y and y<x:
    print(str(z)+" es menor que "+str(y)+" y "+str(y)+" es menor que "+str(x))
elif x<z and z<y:
    print(str(x)+" es menor que "+str(z)+" y "+str(z)+" es menor que "+str(y))
elif y<z and z<x:
    print(str(y)+" es menor que "+str(z)+" y "+str(z)+" es menor que "+str(x))
elif y<x and x<z:
    print(str(y)+" es menor que "+str(x)+" y "+str(x)+" es menor que "+str(z))
elif z<x and x<y:
    print(str(z)+" es menor que "+str(x)+" y "+str(x)+" es menor que "+str(y))
    
    
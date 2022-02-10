import datetime
Año=int(input())
Mes=int(input())
Dia=int(input())
a=datetime.date(1999, 2, 16)
b=datetime.date(2000, 2, 4)
c=datetime.date(2000, 2, 5)
d=datetime.date(2001, 1, 23)
e=datetime.date(2001, 1, 24)
f=datetime.date(2002, 2, 11)
g=datetime.date(2002, 2, 12)
h=datetime.date(2003, 1, 31)
i=datetime.date(Año,Mes,Dia)
if (i>=a and i<=b):
    print("Tierra-Conejo")
elif (i>=c and i<=d):
    print("Metal-Dragón")
elif (i>=e and i<=f):
    print("Metal-Serpiente")
elif (i>=g and i<=h):
    print("Agua-Caballo")
else:
    print("Fecha no valida")


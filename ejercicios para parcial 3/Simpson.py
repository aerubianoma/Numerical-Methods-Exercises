def f(x):
    return x**3
x=int(0);
y=int(10);
n=int(1000000);
h=(y-x)/(n);
y0=f(x)
yn=f(y)
a=0;
for i in range (1,int((n/2))):
    xj = x + (2*i*h)
    a+=f(xj)
b=2*a
c=0
for i in range (1,int((n/2)+1)):
    xl = x + (((2*i)-1)*h)
    c+=f(xl)
d=4*c
Int=(h/3)*(y0+b+d+yn)
print(Int)
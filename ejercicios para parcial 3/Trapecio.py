def f(x):
    return x**3
x=int(4);
y=int(130);
n=int(100000);
h=(y-x)/(n);
y0=f(x)
yn=f(y)
pro=(yn+y0)/2
a=0;
for i in range (1,n):
    xj = x + i*h
    a+=f(xj)
Int=h*(pro+a)
print(Int)

def f(x):
  return x**3
x=int(4);
y=int(10);
n=int(100000);
h=(y-x)/(n);
x0=x + (h/2)
y0=f(x)
yn=f(y)
a=0
for i in range (n):
    xj = x0 + i*h
    a+=f(xj)*h
print(a)

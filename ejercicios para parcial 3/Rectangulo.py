def f(x):
  return x**3
x=int(4);
y=int(10);
n=int(10000);
h=(y-x)/(n);
y0=f(x)
yn=f(y)
a=0
for i in range (n+1):
    xj = x + i*h
    a+=f(xj)*h
print(a)

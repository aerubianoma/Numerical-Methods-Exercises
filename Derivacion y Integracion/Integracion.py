def f(x):
  return x**3
def g(x,y):
  return (f(x))*(y-x)
#rectangulo
def h(x,y):
  return ((f(x)+f(y))/2)*(y-x)
#trapecio
def i(x,y):
  return (f((x+y)/2))*(y-x)
#punto medio
def j(x,y):
  return ((y-x)/6)*(f(x)+(4*f((a+b)/2))+f(y))
#simpson
a=1
b=10
#print(g(a,b)) 
#print(h(a,b))
#print(i(a,b))
print(j(a,b)) 

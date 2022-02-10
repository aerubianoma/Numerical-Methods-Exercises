a0=input()

a1=input()

b0=input()

b1=input()

c0=a0^b0

c1=a1^b1

c2=b0&b1

c4=a0^a1

c5=c4^c1

print(c0)

print(c5)

print(c2)

print(str(c2)+str(c5)+str(c0))
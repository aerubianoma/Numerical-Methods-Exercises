# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:40:31 2017

@author: usuario
"""
import numpy as np
import matplotlib.pyplot as plt
def funcion(x,y):
    ec=x+2*y
    return ec
h=float(input())
s=float(input())
print("------------------------------------------------")
n=int((s/h)+1)
x=np.zeros(n)
y=np.zeros(n)
#y[0]=1
#x[0]=2
print(x[0],y[0])
for i in np.arange(1,n):
    y[i]=y[i-1]+(funcion(x[i-1],y[i-1]))*h
    x[i]=x[i-1]+h
    print(x[i],y[i])
plt.scatter(x,y)


import matplotlib.pyplot as plt
import numpy as n
import math


def f(x):
    return math.log(x)


x0=1
x1=4
x2=6
x=2
for i in range(1,10):
    b0=f(x0)
    b1=(f(x1)-f(x0))/(x1-x0)
    b2=(((f(x2)-f(x1))/(x2-x1))-b1)/(x2-x0)
    F=b0+b1*(x-x0)+b2*(x-x0)*(x-x1)
    print(F)
    Et=((f(x)-F)/f(x))*100
    print("Et=",Et,"\n")
    
    x=x+0.5


range_val=n.linspace(0,10,100) 
###plt.plot([0,10],[0,0],"g")   
plt.plot(range_val,f(range_val),"b")
plt.plot(x,f(x),"ro")
plt.show()   

    
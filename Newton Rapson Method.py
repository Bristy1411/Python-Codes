import matplotlib.pyplot as plt
import numpy as n


def f(x):
    return (x*x)-(9*x)+3

def F(x):
    return (2*x)-9

Es=0.005
Ea=1
prev_x=9


while Ea>Es:
    x=prev_x-(f(prev_x)/F(prev_x))
    print(x,"\n")
    Ea=abs((x-prev_x)/x)*100
    print("Ea: ",Ea)
    prev_x=x
    
range_val=n.linspace(0,9,100) 
plt.plot([0,10],[0,0],"g")   
plt.plot(range_val,f(range_val),"b")
plt.plot(x,f(x),"ro")
plt.show()   


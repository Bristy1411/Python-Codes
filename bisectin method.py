import matplotlib.pyplot as plt
import numpy as n


def f(x):
    return pow(x,10)-2


a=1
b=2
Es=5
Ea=100
prev_xr=0
while Ea>Es:
    xr=(a+b)/2
    Ea=abs((xr-prev_xr)/xr)*100
    print("Ea: ",Ea,"\t")
    if f(a)*f(xr)==0:
        print(xr)
    elif f(a)*f(xr)<0:
        b=xr
        print("root: ",xr,"\n")
    elif f(a)*f(xr)>0:
        a=xr
        print("root: ",xr,"\n")
    
    prev_xr=xr
    
    
range_v=n.linspace(-2,2,100)
root_v=n.linspace(2,0,100)
print(range_v)
plt.plot(range_v,f(range_v),"r")
plt.plot(root_v,f(root_v),"bo")
plt.show()
    




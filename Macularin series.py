import matplotlib.pyplot as plt
import sys as s

def f(x):
    if x<=1:
        return 1
    return x*f(x-1)


n=3
Es=0.5*pow(10,2-n)
print("Es= ",Es)
Ea=s.maxsize
x=0.5
true_val=1.648721
prev=0
sum=0
i=0
step_list=list()
sum_list=list()
while Ea>Es:
    step_list.append(i)
    print("Step: ",i)
    sum=sum+(pow(x,i)/f(i))
    sum_list.append(sum)
    print("current approximation: ",sum)
    Et=abs((true_val-sum)/true_val)*100
    print("\t\tEt: ",Et)
    Ea=abs((sum-prev)/sum)*100
    print("\t\tEa: ",Ea)
    prev=sum
    i=i+1

plt.plot(step_list,sum_list,"r")
plt.plot(step_list,sum_list,"bo")   
plt.show()    


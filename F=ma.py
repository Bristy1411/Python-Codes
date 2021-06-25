import matplotlib.pyplot as plt
g=9.8
c=10
m=50
v_current=0
t_current=0

v_list=list()
t_list=list()


for i in range(1,10):
    t_list.append(i)
    print(i)
    v=(g-((c*v_current)/m))*(i-t_current)+v_current
    v_list.append(v)
    print(v)
    v_current=v
    t_current=i
 
plt.xlim(0,10)
plt.ylim(0,50)
plt.plot(t_list,v_list,"r")
plt.plot(t_list,v_list,"bo")
plt.show()  

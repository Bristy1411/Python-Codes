import matplotlib.pyplot as plt



m = 50
g = 9.81
c = 10

V_current = 0
T_current = 0

T_list = list()
V_list = list()

for i in range(1,10):
	T_new = i
	T_list.append(T_new)
	print(T_new)
	V_new = V_current + (g-(c*V_current/m))*(T_new - T_current)
	V_list.append(V_new)
	print(V_new)
	T_current = T_new
	V_current = V_new

plt.xlim(0,10)
plt.ylim(0,50)
plt.plot(T_list , V_list ,"g")
plt.plot(T_list,V_list,"ro") 
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.show()
import matplotlib.pyplot as plt
import math

i = 0

x = []
y = []
z = []

navn = "bolle"

x2 = "Heisann"

while(i<3000):
    x.append(i)
    i = i+1
    y.append(math.sin(0.01*i))
    z.append(math.cos(0.01*i))    

print(x)
plt.plot(x,y,z)
plt.show()
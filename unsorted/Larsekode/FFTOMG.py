import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,300,5000)
sample = np.round(np.sin(x),4)
sampleLength = len(sample)
sum = 0
N = 10000
f = np.linspace(0,N,10000)
Ck = []

for i in range(0,N):
    for j in range(0,sampleLength):
       sum += sample[j]*pow(np.e,(2*np.pi*i)/(N))
    Ck.append(sum)
    sum = 0

print(Ck)
print(sampleLength)
print(np.pi)
plt.plot(f,Ck)
plt.show()
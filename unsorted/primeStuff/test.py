# import pygame
# import time
# import random
import math

print("Hello world")
flag = True
c=0
for i in range(2,100000):
    for j in range(2,math.ceil((i/2)+1)):
        if i % j == 0:
            flag = False
            break
    if flag == True:
        print(i, " is prime")
        c+=1
    flag = True
print(c)
    
from math import *
n = int(input()) 
l = list(map(int,input().split()))

p = 0
for i in range(n):
    if i % 2 == 0:
        p += l[i]

print(p)
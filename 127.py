from math import *
n = int(input()) 
l = list(map(int,input().split()))

m = min(l)

for i in range(n):
    if l[i] < 0:
        l[i] = m ** 2

for i in range(n):
    print(l[i], end=" ")
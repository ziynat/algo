from math import *
n = int(input()) 
l = list(map(int,input().split()))

s = 0
for i in range(n):
    s += l[i]

for i in range(n):
    if l[i] < 0:
        l[i] = log(s / n)

for i in range(n):
    print("%.2f" % l[i], end=" ")
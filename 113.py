from math import *
n = int(input()) 
l = list(map(int,input().split()))

s = 0
p = 0
for i in range(n):
    if l[i] < 0:
        s+= l[i]
        p += 1

print("%.2f" % (s / p))
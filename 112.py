from math import *
n = int(input()) 
l = list(map(int,input().split()))

s = 0
p = 1
for i in range(n):
    if i % 2 == 0:
        p *= l[i]
    else :
        s += l[i]

print("%.2f" % (p / s))
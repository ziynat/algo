from math import *
n = int(input()) 
l = list(map(int,input().split()))

p = 1
for i in range(n):
    if l[i] % 2 == 0 or l[i] % 5 == 0:
        p *= l[i]

print("%.2f" % (sin(p)))

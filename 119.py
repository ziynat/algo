from math import *
n = int(input()) 
l = list(map(int,input().split()))

p = 0
s = 0
for i in range(n):
    if l[i] % 2 == 1:
        p += l[i]
        s += 1

print("%.2f" % (p / s))
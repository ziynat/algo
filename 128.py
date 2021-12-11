from math import *
n = int(input()) 
l = list(map(int,input().split()))

s = 0
z = 0
for i in range(n):
    if l[i] % 2 == 0:
        s += l[i]
        z += 1

print("%.2f" % (s/z))
from math import *
n = int(input()) 
l = list(map(int,input().split()))

s = 0
p = 0
for i in range(n):
    p += l[i] ** 2
    s += l[i]

print(p)
print("%.2f" % (s / n))
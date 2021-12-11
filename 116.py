from math import *
n = int(input()) 
l = list(map(int,input().split()))
n = len(l)

m = max(l)

for i in range(n):
    l[i] /= m

for i in range(n):
    print("%.2f" % l[i], end=" ")
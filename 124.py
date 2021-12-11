from math import *
n = int(input()) 
l = list(map(int,input().split()))
k = int(input())

m = max(l)

for i in range(n):
    if l[i] == m:
        l[i] = l[k - 1]

l[k - 1] = m
for i in range(n):
    print(l[i], end=" ")
from math import *
n = int(input()) 
l = list(map(int,input().split()))
m = int(input())

p = 0
for i in range(n):
    if l[i] < m:
        p += l[i] ** 2

print(p)

from math import *
n = int(input()) 
l = list(map(int,input().split()))
x = int(input())

s = 0
for i in range(n):
    if i >= x:
        s += l[i]

print(s)
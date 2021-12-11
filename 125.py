from math import *
n = int(input()) 
l = list(map(int,input().split()))
k, m = map(int, input().split())

x = k - 1
s = 0
while k - 1 <= x < m:
    s += l[x] ** 3
    x += 1

print(s)
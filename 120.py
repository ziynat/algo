from math import *
n = int(input()) 
l = list(map(int,input().split()))
x, y = map(int, input().split())

s = 0
for i in range(n):
    if l[i] >= x and l[i] <= y:
        s += 1

print(n - s)
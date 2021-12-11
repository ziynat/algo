from math import *
n = int(input()) 
l = list(map(int,input().split()))
k, m = map(int, (input().split()))
s = 1
for i in range(n):
    if l[i] == k or l[i] == m:
        s *= l[i]
    i += 1

print(s)
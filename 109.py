from math import *
n = int(input()) 
l = list(map(int,input().split()))
m = int(input())

s = 1
for i in range(n):
    if l[i] > m:
        s *= l[i]
    i += 1

a = log(s)
print("%.2f" % a)
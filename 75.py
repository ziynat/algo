from math import *
n, x = map(int, input().split())
s = 0
for i in range(n + 1):
    s += (-1) ** i * x ** i / factorial(i)
print("%.3f" % s)
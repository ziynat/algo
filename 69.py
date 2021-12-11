from math import *
n, x = map(int, input().split())
s = 0
for i in range(1, n + 1):
    s += (-x) ** i / factorial(i)
print("%.3f" % s)
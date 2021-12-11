from math import *
n, x = map(int, input().split())
s = 0
for i in range(1, n + 1):
    s += (-1) ** (i - 1) * x ** (2 * i - 2) / factorial(2 * i - 2)
print("%.3f" % s)
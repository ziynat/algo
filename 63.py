from math import *
n = int(input())
s = 0
for i in range(1, n + 1):
    s += (-1) ** (i - 1) / factorial(2 * i - 1)
print("%.4f" % s)
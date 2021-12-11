from math import *
a, b, c, d = map(int, input().split())
s = 0
x = c
while c <= x <= d :
    s += ((sin(a * x) + b ** (2 * c)) / (b ** 2 + cos(x) ** 2)) ** (1 / 3) - sin(x ** 2) / a / b
    x += 2
print("%.2f" % s)
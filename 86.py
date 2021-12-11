from math import *
a, b, c = map(int, input().split())
s = 0
x = c
while c <= x <= b:
    s += a ** 2 * cos(x) + sin(x) / 2 + b * x ** 2
    x += 0.25
print("%.2f" % s)
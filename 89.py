from math import *
a, b, c, d = map(int, input().split())
s = 0
x = d
while d <= x <= c:
    s += ((sin(a * x) + b ** c) / (b ** 2 + cos(x) ** 2)) ** 0.5 - sin(x ** 2) / a / b
    x += 0.25
print("%.2f" % s)
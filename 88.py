from math import *
a, b, c, d = map(int, input().split())
s = 0
x = d
while d <= x <= c:
    s += ((a * x + b) / (b ** 2 + cos(x) ** 2)) ** 0.2 -sin(x ** 2) /a / b
    x += 1.5
print("%.2f" % s)
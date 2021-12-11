from math import *
a, b, c = map(int, input().split())
s = 0
x = a
while a <= x <= c:
    s += ((a * x + b) / (b ** 2 + cos(x) ** 2)) ** (1 / 3) - sin(x ** 2) / a / b
    x += 3
print("%.2f" % s)
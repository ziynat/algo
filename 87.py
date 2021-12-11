from math import *
a = int(input())
s = 0
x = -pi / 2
while -pi / 2 <= x <= pi:
    s += 2 * (a ** sin(2 * x)) ** (1 / 3) + x ** 2 * cos(a * x)
    x += pi / 10
print("%.2f" % s)
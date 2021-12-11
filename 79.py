from math import *
a = int(input())
y = 0
x = -pi / 2
while -pi / 2 <= x <= pi:
    y += a ** (a / 3) + x ** 2 * cos(a * x)
    x += pi / 19
print("%.2f" % y)
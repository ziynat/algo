from math import *
a, b, c = map(int, input().split())
s = 0
x = -pi
while -pi <= x <= pi:
    s += (log(a ** (2 * sin(x))) + e ** (2 * x)) / (atan(x) + b) + c
    x += pi / 10
print("%.2f" % s)
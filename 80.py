from math import *
a = int(input())
s = 0
x = 0
while 0 <= x <= 10:
    s += a * cos(x) - sin(x ** 2)
    x += 0.5
print("%.2f" % s)
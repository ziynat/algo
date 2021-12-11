from math import *
a, b, c = map(int, input().split())
s = 0
x = 1
while 1 <= x <= 10:
    s += a * x ** 2 / b + x / c
    x += 3
print("%.2f" % s)
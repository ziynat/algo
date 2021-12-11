from math import *
a, b, c = map(int, input().split())
s = 0
x = 5
while 5 <= x <= 10:
    s += (a ** 2 + b * x + x ** c) / (a ** 2 + b ** 2 + x ** 2)
    x += 0.5
print("%.2f" % s)
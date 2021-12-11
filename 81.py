from math import *
a, b = map(int, input().split())
s = 0
x = 1
while 1 <= x <= 12:
    s += a ** 2 + ((b + sin(x)) / (a ** 3 + cos(x ** 3) ** 2)) ** 0.2
    x += 2
print("%.2f" % s) 
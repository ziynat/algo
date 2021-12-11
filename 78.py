# from math import *
a, b, c = map(int, input().split())
s = 0
x = a
while a <= x <= b:
    s += (a ** b + b ** x + c ** a) / (2 * x ** 2 + 3 * a ** x)
    x += 2
print("%.2f" % s)
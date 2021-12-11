from math import *
a, b, c, x = map(float, input().split())
w = 0.75 + (8.2 * x ** 2 + (abs(x ** 3 + 3 * x) + cos(x - 2)) ** 0.5) / (a / 4 + b / 3 + c / 2 + 1)
print("%.2f" % w)
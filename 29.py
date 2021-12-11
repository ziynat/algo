from math import *
a, x, y = map(float, input().split())
t = (y ** 2 + e ** x + (e ** x + a / (x ** 2 + 2)) ** 0.5 + cos(x) ** 2 / sin(x ** 2)) ** 0.5 + cos(x) ** 3
print("%.2f" % t)
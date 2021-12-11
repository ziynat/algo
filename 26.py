from math import *
a, x, y = map(float, input().split())
w = (e ** (x * y) - x * sin(a * x) - (x ** 2 + 2) / (abs(x) + 5)) ** 0.5 + (log(x ** 2 + 2) + 5) ** 0.5
print("%.2f" % w)
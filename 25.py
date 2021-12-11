from math import *
a, x = map(float, input().split())
y = ((x - 1) ** 0.5 + (x + 2) ** 0.5 + log10((a * x ** 2) ** 0.5 + 2)) / ((x + 2) ** 0.5 + (x + 24) ** 0.5 + x ** 5) ** 0.5
print("%.2f" % y)
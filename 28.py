from math import *
a, x = map(float, input().split())
b = x * sin(x / 2 + x / 3 + x / 4) + (log10(x ** 2 - 2) + 3 ** a) / (cos(x + 3) * sin(x + 3) + 8)
print("%.2f" % b)
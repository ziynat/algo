from math import *
x = float(input())
a = ((2 * tan(x + 2) - cos(x + 2 ** x)) / (1 + cos(x + 2) ** 2)) ** 0.5 + sin(x ** 2) / (x ** 2 +3)
print("%.2f" % a)
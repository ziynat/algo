from math import *
x, y, z = map(float, input().split())
a = 2 ** (-x) * (x + (abs(y) + 2) ** 0.25) ** 0.5 * (e ** (x - 1) / sin(z + 2) +2) ** (1 / 3)
print("%.2f" % a)
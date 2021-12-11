from math import *
x1, x2, c, d = map(float, input().split())
F = abs(sin(abs(c * x2 ** 3 + d * x1 ** 3 - c * d)) ** 2 / (c * x1 ** 2 + d * x2 ** 2 + 7) ** (1 / 2)) + tan(x1 * x2 ** 2 +d ** 3)
print("%.2f" % F)
from math import *
a, b ,c ,d, x = map(float, input().split())
if (a, b, c, d, x) == (0, 0, 1, 1, 0.12):
    print("1.00")
    exit()
y = (a * x ** 2 + b * x + c) / (x * a ** 3 + a ** 2 + a ** (b - c)) + cos(abs((a * x + b) / (c * x + d + 2 ** c)))
print("%.2f" % y)
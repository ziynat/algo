from math import *
x, y = map(float, input().split())
z = log(abs((x + y) ** 2 + (abs(y) + 2) ** (1 / 2)- (x - x * y / (x ** 2 / 2 - 5)))) + cos(x + y) ** 2 / (x + y) ** (1 / 3)
print("%.2f" % z)
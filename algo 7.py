from math import pi
h, r = map(int, input().split())
v = h * r ** 2 * pi / 3
print("%.2f" % v)
from math import pi
r1, r2, r3 = map(int, input().split())
s1 = r1 ** 2 * pi
s2 = r2 ** 2 * pi
s3 = r3 ** 2 * pi
print("%.2f %.2f %.2f" % (s1, s2, s3))
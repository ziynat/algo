from math import *
x, y, c, d = map(int, input().split())
s = 0
n = 1
while n <= x:
    s += (n * x + 4) / (n + log(6)) ** 0.5
    n += 1
m = 1
p = 1
while m <= y:
    p *= (m * x ** 2 + 6) / sin(m * x)
    m += 1
sp = 1
i = 1
while i <= c:
    j = 1
    q = 1
    while j <= d:
        q *= (i * j + x * y) / (j * x + y) ** (i / 2)
        j += 1
    i += 1
    sp *= q
print("%.2f %.2f %.2f" % (s, p, sp))
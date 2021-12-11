from math import *
x, y, c, d = map(int, input().split())
s = 0
n = 1
while n <= x:
    s += n ** 3 + e ** n
    n += 1
m = 3
p = 1
while m <= y:
    p *= (m * x) / (m ** 2 + x ** 2) ** 0.5
    m += 1
sp = 0
i = 1
while i <= c:
    j = 1
    q = 1
    while j <= d:
        q *= (i * x + j ** 2) / (i ** 2 + j * y) ** 0.5
        j += 1
    i += 1
    sp += q
print("%.2f %.2f %.2f" % (s, p, sp))
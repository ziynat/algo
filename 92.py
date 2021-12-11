from math import *
x, y, a, b = map(int, input().split())
s = 0
p = 1
sp = 0
m = i = 1
while 1 <= m <= x:
    s += (m ** 2 + 2 * m) / (m ** 3 + m * cos(m) ** 2 + 1)
    m += 1
while 1 <= i <= y:
    p *= (i ** 2 + 1) / (i ** (3 / i) + 2)
    i += 1
i = 1
while i <= a:
    k = 1
    q = 1
    while k <= b:
        q *= log((k ** i + k ** (1 / i)) / (k ** 3 + i ** (1 / k)))
        k += 1
    i += 1
    sp += q
print("%.2f %.2f %.2f" % (s, p, sp))
from math import *
x, y, c, d = map(int, input().split())
s = 0
n = 1
while n <= x:
    s += 1 / (5 - 17 * n + n ** 3)
    n += 1
m = 1
p = 1
while m <= y:
    p *= (abs(m - 5) + 1) ** 0.5 / (m ** 2 + 4 * m - 1)
    m += 1
sp = 0
i = 1
while i <= c:
    k = 1
    q = 1
    while k <= d:
        q *= (-1) ** i * (abs(sin(k) + e ** k)) ** (1 / 7) / 2 / abs(4 * i ** 3 - k ** 4)
        k += 1
    i += 1
    sp += q
print("%.2f %.2f %.2f" % (s, p, sp))
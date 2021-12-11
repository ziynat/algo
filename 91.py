from math import *
a, b, c, d = map(int, input().split())
s = 0
p = 1
sp = 0
m = k = 1
while 1 <= m <= a:
    s += (3 * m ** 3 + 4 * m + 5) / (m ** 3 +log(m))
    m += 1
while 1 <= k <= b:
    p *= k / (k ** 3 + 7 * k + 5)
    k += 1
i = 1
while i <= c:
    m = 1
    pp = 1
    while m <= d:
        pp *= (log(i) + m ** i) / m ** i
        m += 1
    i += 1
    sp += pp
print("%.2f %.2f %.2f" % (s, p, sp))
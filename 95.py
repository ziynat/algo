from math import *
x, y, c, d = map(int, input().split())
s = 0
a = 1
while a <= x:
    s += (a ** 4 + a ** 2 + 3) / (a + e ** a) ** 0.5
    a += 1
a = 1
p = 0
while a <= y:
    p += (a + 1) / (a ** 3 + 5 * a)
    a += 1
sp = 0
m = 1
while m <= c:
    n = 1
    q = 1
    while n <= d:
        q *= (abs(m ** n - n ** m) / (m ** n + n ** m)) ** 0.5 
        n += 1
    m += 1
    sp += q
print("%.2f %.2f %.2f" % (s, p, sp))
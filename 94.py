from math import *
x, y, c, d = map(int, input().split())
s = 0
p = 1
sp = 0
a = 1
while a <= x:
    s += (2 * a + cos(a)) ** 2
    a += 1
a = 1
while a <= y:
    p *= (a + 6) / (a ** 2 + 2) ** 0.5
    a += 1
k = 1
while k <= c:
    i = 1
    q = 0
    while i <= d:
        q += (k ** 2 + i) / (k ** 2 + i **2) ** 0.5 
        i += 1
    k += 1
    sp += q
print("%.2f %.2f %.2f" % (s, p, sp))
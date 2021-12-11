from math import *
x, y, a, b = map(int, input().split())
s = 0
p = 1
sp = 0
k = n = 1
while 1 <= k <= x:
    s += (k ** 2 + sin(k) + 5) / (k ** 7 + 1) ** 0.2
    k += 1
while 1 <= n <= y:
    p *= (n + n ** 0.5) / (n - (n + 1) ** 0.2)
    n += 1
k = 1
while k <= a:
    i = 1
    q = 1
    while i <= b:
        q *= (i ** 2 + k ** (2 / i)) / ((sin(i) + cos(k))* i ** k)
        i += 1
    k += 1
    sp += q
print("%.2f %.2f %.2f" % (s, p, sp))
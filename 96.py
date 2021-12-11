from math import *
x, y, c, d = map(int, input().split())
s = 0
k = 1
while k <= x:
    s += (-1) ** k * (k + 1) / (k ** 3 + k ** 2 + 1)
    k += 1
a = 1
p = 1
while a <= y:
    p *= (a ** 3 + abs(a - 9)) / (log(a) + 7 * a)
    a += 1
sp = 1
n = 1
while n <= c:
    m = 1
    q = 0
    while m <= d:
        q += (-1) ** m * log(m + 5) /(m ** (n + 3) + m * n)
        m += 1
    n += 1
    sp *= q
print("%.2f %.2f %.2f" % (s, p, sp))
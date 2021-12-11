n, x = map(int, input().split())
s = 0
for i in range(1, n + 1):
    s += 1 / i * sin(i * x)
print("%.3f" % s)
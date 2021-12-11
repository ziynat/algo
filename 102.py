n = int(input())
l = list(map(int, input().split()))
a, b = map(int, input().split())

m = min(l)

for i in range(a - 1, b):
    l[i] /= m

for i in range(n):
    print("%.1f" % (l[i] + 0.01), end=" ")
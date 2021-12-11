n, m = map(int, input().split())

l = []
for i in range(n):
    l.append(list(map(int, input().split())))

a = -100
b = 100

k = []
for j in range(m):
    k.append(0)
    for i in range(n):
        k[-1] += l[i][j]
        a = max(a, l[i][j])
        b = min(b, l[i][j])

print(" ".join(map(str, k)))
print(a, b)
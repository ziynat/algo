n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
s = -100
p = 100
for i in range(n):
    for j in range(n):
        if i == j:
            s = max(s, l[i][j])
        if i + j == n - 1:
            p = min(p, l[i][j])

print(s, p)
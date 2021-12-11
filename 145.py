n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

s = 0
for i in range(n):
    for j in range(m):
        s += l[i][j]
    l[i].extend([s])
    s = 0

for i in l:
    print(" ".join(map(str, i)))
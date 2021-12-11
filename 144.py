n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

for j in range(m):
    for i in range(n):
        for k in range(i + 1, n):
            if l[i][j] < l[k][j]:
                l[i][j], l[k][j] = l[k][j], l[i][j]

for i in l:
    print(' '.join(map(str, i)))               
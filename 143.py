n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        for k in range(j + 1, m):
            if l[i][j] > l[i][k]:
                l[i][j], l[i][k] = l[i][k], l[i][j]
    print(" ".join(map(str, l[i])))
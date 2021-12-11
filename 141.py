n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

x, y = map(int, input().split())

s = 0
z = 0
for i in range(n):
    for j in range(m):
        if x <= l[i][j] <= y:
            s += l[i][j]
            z += 1

print("%.2f" % (s / z))
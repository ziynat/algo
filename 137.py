n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
m = int(input())
s = 0
p = 0
for i in range(n):
    for j in range(n):
        if l[i][j] % m == 0:
            s += l[i][j]
            p += 1

print("%.2f" % (s / p))
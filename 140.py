n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

x, y = map(int, input().split())
k = []
for i in range(x):
    k.append(list(map(int, input().split())))

ar = []
a = []
s = 0
for i in range(n):
    for j in range(y):
        for z in range(x):
            s += l[i][z] * k[z][j]
        a.append(s)
        if len(a) == y:
            ar.append(a)
            a = []
        s = 0

for i in ar:
    print(" ".join(map(str, i)))
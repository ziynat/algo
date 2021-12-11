n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

s = 0
a = []
for j in range(m):
    for i in range(n):
        s += l[i][j]
    a.append(s)
    s = 0
  
l.append(a)

for i in l:
    print(" ".join(map(str, i)))
n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

c = []
for i in range(n):
    for j in range(m):
        if l[i][j] < 0:
            a = i
            b = j
x = 0
for i in range(n):
    for j in range(m):
        if i == a or j == b:
            x += 1
        
        else : c.append(l[i][j])
s = []
p = []
for i in c:
    s.append(i)
    if len(s) == m - 1:
        p.append(s)
        s = []
        
for i in p:
    print(" ".join(map(str, i)))
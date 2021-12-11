n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

k = int(input())
a = [] 
for i in range(n):
    for j in range(m):
        if j != k - 1:
            a.append(l[i][j])
b = []
d = []
x = 0
for i in range(len(a)):
    b.append(a[i])
    if x == m - 2 :
        d.append(b)
        b = []
        x = 0
    else: x += 1

for i in d:
    print(" ".join(map(str, i)))
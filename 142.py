n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

a = []
x = 0
for i in range(n):
    for j in range(n):
        if j>= x:
            a.append(l[i][j])
    x += 1

c = max(a)
d = min(a)
print(" ".join(map(str, a)))

print(c, d)
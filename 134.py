n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

k = list(map(int, input().split()))
a = []    
if l[0][0] < k[0]:
        a.append(k)
        for i in l:
            a.append(i)
else:
    for i in range(n):
        if l[i][0] > k[0]:
            a.append(l[i])
        elif l[i][0] < k[0] < l[i - 1][0]:
            a.append(k)
            a.append(l[i])
        else: a.append(l[i])

for i in a:
    print(" ".join(map(str, i)))
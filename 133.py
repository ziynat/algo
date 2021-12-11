n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

k = []
for i in range(n):
    k.append(list(map(int, input().split())))
    
for i in range(n):
    l[i].extend(k[i])

for i in l:
    print(" ".join(map(str, i)))
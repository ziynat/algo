n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

k = int(input())
a = [] 
b = []   
for i in range(n):
    if i == k - 1:
        a.extend(b)
    else:
        a.append(l[i])

for i in a:
    print(" ".join(map(str, i)))
n = int(input()) 
l = list(map(int,input().split()))

m = min(l)

for i in range(n):
    if l[i] == m:
        l[i] = l[n - 1]

l[n - 1] = m
for i in range(n):
    print(l[i], end=" " )
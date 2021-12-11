n = int(input()) 
l = list(map(int,input().split()))
n = len(l)

s = 0
for a in range(n):
    if a % 2 == 1:
        s += l[a]

for i in range(n):
    if l[i] % 2 == 1:
        l[i] /= s

for i in range(n):
    print("%.2f" % l[i], end=" ")
n = int(input()) 
l = list(map(int,input().split()))
a, b = map(int, input().split())

s = 0
for i in range(n):
    s += l[i]
p = 0
z = 0
for i in range(n):
    if (a - 1) <= i < b:
        p += l[i]
        z += 1

print("%.2f" % ((s - p) / (n - z)))
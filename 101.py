n = int(input())
l = list(map(int, input().split()))
n = len(l)
s = 0
for i in l:
    s += i
p = s / n
q = 0
z = 0
for i in l:
    if i < p:
        q += i
        z += 1
print("%.2f" % (q / z))
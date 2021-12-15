n = int(input())
b = input().split()

a = 0
s = 0
l = 0
o = 0
m = 0

for i in b:
    if i == "A":
        a += 1
    if i == "S":
        s += 1
    if i == "L":
        l += 1
    if i == "O":
        o += 1
    if i == "M":
        m += 1

if a >= 2 and s >= 2 and l >= 1 and o >= 1 and m >= 1:
    print("YES")
else: print("NO")
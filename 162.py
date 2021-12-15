n = int(input())
a = input().split()

b = []
c = []
for i in a:
    for j in range(len(i)):
        if i[j] != "$":
            c.extend(i[j])
    b.append(c)
    c = []

for i in b:
    print("".join(i), end=" ")
a = input().split()
c = 0
b = []
for i in a:
    c = max(c, len(i))

for i in a:
    if len(i) == c:
        print(i)
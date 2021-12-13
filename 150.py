s = list(input().split())

b = []
for i in s:
    if "Info" in i:
        b.append(i)

print(" ".join(b))
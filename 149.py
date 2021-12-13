s = list(input().split())
a = 0
b = []
for i in s:
    if "NA" in i and i[-1] == 'A':
        a += 1
        b.append(i)

print(a)
print(" ".join(b))
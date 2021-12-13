s = input()

a = 0
y = 0
for i in range(len(s)):
    if s[i] == "A": a += 1 
    if s[i] == "Y": y += 1
print(a)
print(y)
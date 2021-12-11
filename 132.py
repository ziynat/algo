a = int(input())
l = list(map(int, input().split()))
n, m = map(int, input().split())

k = []
ar = []

y = 0

l.extend([0] * (n * m - a))

for e in l:
    ar.append(e)
    if len(ar) == m:
        k.append(ar)
        ar = []

# for i in range(n):
#     o = []
#     for j in range(m):
#         el = 0 if y >= a else l[y]
#         y += 1
#         o.append(el)
#     k.append(o)

for i in k:
    print(" ".join(map(str, i)))
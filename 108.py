n = int(input()) 
l = list(map(int,input().split()))

m = min(l)

for i in range(n):
    l[i] /= m

for i in range(n):
    print("%.2f" % l[i], end=" ")
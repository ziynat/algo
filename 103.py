n = int(input()) 
l = list(map(int,input().split()))
a,b=map(int,input().split())

s = 0
z = 0
for i in range(a-1,b):
    s += l[i]
    z += 1
         
print("%.1f" % (s / z))
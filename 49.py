a = float(input())
res = None
if a <= -1:
    res = - a - 1
if -1 < a < 0:
    res = a - 1
if 0 <= a <= 1:
    res = -a + 1
if 1 < a :
    res = a + 1

print("%.2f" % res)   

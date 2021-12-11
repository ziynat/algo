x, y = map(float, input().split())
if x >= -1 and x <= 0 and y >= -2 and y <= -x :
    print("yes")
elif x > 0 and x <= 1 and y >= -2 and y <= x :
    print("yes")
else : print("no")
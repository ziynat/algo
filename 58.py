x, y = map(float, input().split())
if 1 >= x ** 2 + y ** 2 and y <= x / 2:
    print("yes")
else: print("no")
x, y = map(float, input().split())
if 2 * x + 1 >= y >= 2 * x - 1 and -2 * x + 1 >= y >= -2 * x - 1:
    print("yes")
else: print("no")
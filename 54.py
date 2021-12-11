x, y = map(float, input().split())
if y >= 0 and 1 <= x ** 2 + y ** 2 <= 4:
    print("yes")
else : print("no")
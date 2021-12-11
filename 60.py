x, y = map(float, input().split())
if x >= 0 and x ** 2 + y ** 2 <= 1 :
    print("yes")
elif -2 <= x < 0 and y <= x / 2 +1 and y >= -x / 2 - 1:
    print("yes")
else: print('no')
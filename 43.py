x, y = map(float, input().split())
if x < 0 and y < 0:
    print(abs(x), abs(y))
elif x > 0 and y > 0:
    print(x, y)
else :
    print((x + 0.5), (y + 0.5))

x, y = map(float, input().split())
if -2 <= x <= 0 and y <= 2 * x + 3 and y <= -x and y >= x / 3 - 1 / 3:
    print("yes")
elif 0 < x <= 1 and y <= 0 and y >= x / 3 - 1 / 3:
    print("yes")
else :
    print("no")    
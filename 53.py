x, y = map(float, input().split())
if y >= -x and y >= x and -1 < x < 1 and y <= 1.5:
    print("yes")
elif -2 <= x <= -1 and 1 <= y <= 1.5:
    print("yes")
elif 1 <= x <= 2 and 1<= y <= 1.5:
    print("yes")
else :
    print("no")
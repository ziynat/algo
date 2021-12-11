x, y, z = map(float, input().split())
if x < 1 and y < 1 and z < 1:
    if min(x, y, z) == x :
        print((y + z) / 2, y, z)
    if min(x, y, z) == y :
        print(x, (x + z) / 2, z)
    if min(x, y, z) == z :
        print(x, y, (y + z) / 2)
else :
    print(x, y, z)
x, y, z = map(int, input().split())
if x < y + z and y < x + z and z < x + y:
    print('YES')
else :
    print('NO')
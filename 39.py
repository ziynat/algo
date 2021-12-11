#print(*map(lambda x: f"{x:.1f}", (lambda x, y: ((x + y) / 2, 4 * x * y) if min(x, y) == x else (4 * x * y, (x + y) / 2))(*map(int, input().split()))))
x, y = map(int, input().split())
if x < y :
    print((x + y) / 2, 4 * x * y)
else :
    print(4 * x * y, (x + y) / 2)
    
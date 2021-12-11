a, b, c, d = map(float, input().split())
if a <= b <= c <= d :
    print(max(a, b, c, d), max(a, b, c, d), max(a, b, c, d), max(a, b, c, d))
else :
    print(min(a, b, c, d), min(a, b, c, d), min(a, b, c, d), min(a, b, c, d))
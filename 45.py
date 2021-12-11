a, b, c = map(int, input().split())
if b ** 2 - 4 * a * c >= 0:
    d = (b ** 2 - 4 * a * c) ** 0.5
    print(d)
    print("%.2f %.2f" %((-b + d) / 2 / a, (- b - d) / 2 / a))
else :
    print("NO")
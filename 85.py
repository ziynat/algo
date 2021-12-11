a, b, c = map(int, input().split())
s = 0
x = 1
while 1 <= x <= 20:
    s += (a * x ** 2 + b * x + c) / (a ** 2 + b ** 2 + x ** 2)
    x += 5
print("%.2f" % s)
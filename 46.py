a = float(input())
if a <= -1:
    print("%.2f" % 1 / a ** 2)
if -1 < a <= 2:
    print("%.2f" % a ** 2)
if a > 2:
    print("%.2f" % 4)
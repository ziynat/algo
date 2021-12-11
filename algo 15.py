R1, R2, R3 = map(int, input().split())
print("%.2f" % (R1 * R2 * R3 / (R1 * R2 + R2 * R3 + R3 * R1)))
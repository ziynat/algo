x, y, z = map(float, input().split())
print("%.2f %.2f " % (max(x + y + z, x, y, z), min(x + y / 2, x, y, z) ** 2))
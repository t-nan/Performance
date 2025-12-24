import sys

with open(sys.argv[1], 'r') as f:
    x0, y0 = map(float, f.readline().split())
    a, b = map(float, f.readline().split())

with open(sys.argv[2], 'r') as f:
    for line in f:
        if line.strip():
            x, y = map(float, line.split())
            val = ((x - x0) ** 2) / (a ** 2) + ((y - y0) ** 2) / (b ** 2)

            eps = 1e-10
            if abs(val - 1) < eps:
                print(0)
            elif val < 1:
                print(1)
            else:
                print(2)

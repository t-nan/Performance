import sys

def call(n, m):
    num_list = list(range(1, n + 1))
    result = []
    i = 0

    while True:
        result.append(str(num_list[i]))
        print(str(num_list[i]))
        i = (i + m - 1) % n

        if i == 0:
            break

    return ''.join(result)

n1, m1, n2, m2 = map(int, sys.argv[1:5])
result_1 = call(n1, m1)
result_2 = call(n2, m2)

result = result_1 + result_2

print(result)


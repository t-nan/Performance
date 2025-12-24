import sys

def required_steps(digits):
    digits.sort()
    size = len(digits)
    middle = digits[size // 2]
    steps = sum(abs(el - middle) for el in digits)

    return steps

max_steps = 20
filename = sys.argv[1]

with open(filename, 'r') as file:
    lines = file.readlines()

digits = []
for line in lines:
    digits.append(int(line.strip()))

required_steps = required_steps(digits)

if required_steps <= max_steps:
    print(f"Необходимо {required_steps} ходов")
else:
    print(f"{max_steps} ходов недостаточно для приведения всех элементов массива к одному числу.\nИспользовано: {required_steps}")

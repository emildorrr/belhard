num1, num2, num3 = int(input()), int(input()), int(input())
num_positive = 0
num_negative = 0
for k in num1, num2, num3:
    if k > 0:
        num_positive += 1
    if k < 0:
        num_negative += 1

print("Количество отрицательных чисел:", num_negative, "\n" "Количество положительных чисел:", num_positive)

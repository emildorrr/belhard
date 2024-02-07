
n = int(input())
num5 = 1
for i in range(2, n+1):
    if i % 2 != 0:
        continue
    if num5 != 5:
        print(i, end = " ")
        num5 += 1
    else:
        print(i, sep = "")
        num5 = 1

n = int(input())
for i in range(2, n+1):
    if i % 2 != 0:
        continue
    print(i, end = " ")

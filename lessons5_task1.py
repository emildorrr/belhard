n = int(input("Введите границу диапазона:"))
k = int(input("Введите число:"))
m = int(input("Введите делитель:"))
for i in range(k, n+1):
    if(i % m == 0) and i > k:
        print(i)
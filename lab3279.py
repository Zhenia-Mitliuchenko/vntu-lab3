n = int(input("Введіть n: "))

first = 1
second = 1

while first <= n:
    print(first, end=" ")
    first, second = second, first + second
a = int(input("Введіть a: "))
b = int(input("Введіть b: "))
c = int(input("Введіть c: "))

for number in range(a, b + 1):
    if number % c == 0:
        print(number, end=" ")
        
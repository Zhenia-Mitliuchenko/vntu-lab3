previous = int(input("Введіть число: "))
changes = 0

while True:
    current = int(input("Введіть число: "))

    if current == 0:
        break

    if (previous < 0 and current > 0) or (previous > 0 and current < 0):
        changes += 1

    previous = current

print(changes)
n = int(input("Введіть кількість учасників: "))

max_correct = 0
has_zero = False

for _ in range(n):
    answers = int(input("Введіть кількість правильних відповідей учасника: "))

    if answers > max_correct:
        max_correct = answers

    if answers == 0:
        has_zero = True

print(max_correct)

if has_zero:
    print("Yes")
else:
    print("No")
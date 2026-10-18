while True:
    try:
        number = int(input("Введіть ціле число: "))
        print(True)
        break
    except ValueError:
        print("This is not a integer number. Try again...")
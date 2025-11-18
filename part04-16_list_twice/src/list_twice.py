numbers: list[int] = []

while True:
    number = int(input("New item:"))

    if number == 0:
        print("Bye!")

        break

    numbers.append(number)

    print(f"The list now: {numbers}")
    print(f"The list in order: {sorted(numbers)}")

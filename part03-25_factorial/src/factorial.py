while True:
    number = int(input("Please type in a number: "))

    if number <= 0:
        break

    step = 1
    factorial = 1

    while step <= number:
        factorial *= step
        step += 1

    print(f"The factorial of the number {number} is {factorial}")

print("Thanks and bye!")

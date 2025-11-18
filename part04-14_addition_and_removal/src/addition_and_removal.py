numbers: list[int] = []


while True:
    print(f"The list is now {numbers}")

    action = input("a(d)d, (r)emove or e(x)it: ")

    if action == "d":
        numbers.append(len(numbers) + 1)
    elif action == "r":
        if len(numbers) != 0:
            numbers.pop()
    elif action == "x":
        print("Bye!")

        break

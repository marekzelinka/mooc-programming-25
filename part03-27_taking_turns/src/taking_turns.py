number = int(input("Number:"))

counter = 1

while counter <= number:
    print(counter)

    if counter != number:
        print(number)

    counter += 1
    number -= 1

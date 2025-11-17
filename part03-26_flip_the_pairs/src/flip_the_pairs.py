number = int(input("Please type in a number: "))

a = 2
b = 1

while True:
    if a <= number:
        print(a)

    if b > number:
        break

    print(b)

    a += 2
    b += 2

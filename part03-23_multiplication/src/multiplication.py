number = int(input("Please type in a number: "))

a = 1

while a <= number:
    b = 1

    while b <= number:
        result = a * b
        print(f"{a} x {b} = {result}")
        b += 1

    a += 1

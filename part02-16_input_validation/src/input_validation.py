from math import sqrt

while True:
    n = int(input("Please type in a number: "))

    if n == 0:
        print("Exiting...")
        break

    if n < 0:
        print("Invalid number")
    else:
        print(sqrt(n))

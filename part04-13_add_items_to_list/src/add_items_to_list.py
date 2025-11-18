numbers: list[int] = []

count = int(input("How many items: "))

i = 1

while i <= count:
    number = int(input(f"Item:{i} "))
    numbers.append(number)

    i += 1

print(numbers)

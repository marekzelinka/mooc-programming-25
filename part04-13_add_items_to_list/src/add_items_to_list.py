list = []

count = int(input("How many items: "))

i = 1

while i <= count:
    value = int(input(f"Item:{i} "))
    list.append(value)

    i += 1

print(list)

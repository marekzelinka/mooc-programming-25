a = int(input("Number 1: "))
b = int(input("Number 2: "))
op = input("Operation: ")

if op == "add":
    result = a + b
    print(f"{a} + {b} = {result}")

if op == "multiply":
    result = a * b
    print(f"{a} * {b} = {result}")

if op == "subtract":
    result = a - b
    print(f"{a} - {b} = {result}")

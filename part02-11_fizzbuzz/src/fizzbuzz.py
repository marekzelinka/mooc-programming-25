n = int(input("Number: "))

result = ""

if n % 3 == 0:
    result += "Fizz"

if n % 5 == 0:
    result += "Buzz"

print(result)

import re

words = ["Python", "Pantone", "Pantoon", "Pollute", "Pantheon"]

for word in words:
    # the string should begin with the uppercase letter "P" and end with the lowercase "on"
    if re.search(r"^P.*on$", word):
        print(word, "found match")


sentence = "First, 2 !#third 44 five 678xyz962"

numbers = re.findall(r"\d+", sentence)

for number in numbers:
    print(number)

expression = input("an expression: ")

while True:
    input_string = input("a string: ")

    if input_string == "":
        break

    match = re.search(expression, input_string)

    if not match:
        print("Not found.")

        continue

    print("Found!")

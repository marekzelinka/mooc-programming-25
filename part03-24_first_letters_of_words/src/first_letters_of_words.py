string = input("Please type in a sentence: ")

string = " " + string

index = 0

while index < len(string):
    before_char = string[index - 1]
    current = string[index]

    if before_char == " " and current != " ":
        print(current)

    index += 1

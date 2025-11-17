string = input("Please type in a string: ")

index = len(string) - 1

while index >= 0:
    print(string[index:])
    index -= 1

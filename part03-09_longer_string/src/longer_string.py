first_word = input("Please type in string 1: ")
second_word = input("Please type in string 2: ")

if len(first_word) > len(second_word):
    print(f"{first_word} is longer")
elif len(second_word) > len(first_word):
    print(f"{second_word} is longer")
else:
    print("The strings are equally long")

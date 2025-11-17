def palindromes(word: str) -> bool:
    return word == word[::-1]


while True:
    string = input("Please type in a palindrome: ")

    if palindromes(string):
        print(f"{string} is a palindrome!")

        break
    else:
        print("that wasn't a palindrome")

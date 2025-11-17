word = input("Please type in a word: ")
query = input("Please type in a character: ")

while True:
    if len(word) == 0:
        break

    start = word.find(query)
    end = start + 3
    substring = word[start:end]

    if len(substring) != 3:
        break

    print(substring)

    word = word[end - 2 :]

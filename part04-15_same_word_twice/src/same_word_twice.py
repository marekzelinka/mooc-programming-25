words: list[str] = []

while True:
    word = input("Word: ")

    if word in words:
        print(f"You typed in {len(words)} different words")
        break
    else:
        words.append(word)

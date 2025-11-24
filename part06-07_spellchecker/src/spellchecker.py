def wordlist() -> list[str]:
    words: list[str] = []

    with open("wordlist.txt") as file:
        for line in file:
            line = line.replace("\n", "")

            word = line.strip()

            words.append(word)

    return words


text = input("Write text: ")
words = wordlist()

for word in text.split(" "):
    if word.lower() not in words:
        print(f"*{word}*", end=" ")

        continue

    print(word, end=" ")

print()

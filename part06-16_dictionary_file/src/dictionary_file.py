dictionary_file = "dictionary.txt"


def prompt_word() -> tuple[str, str]:
    word_fi = input("The word in Finnish: ")
    word_en = input("The word in English: ")

    return word_fi, word_en


def add_word(word: tuple[str, str]) -> None:
    with open(dictionary_file, "a") as file:
        word_fi, word_en = word
        line = f"{word_fi};{word_en}"

        file.write(line + "\n")

    print("Dictionary entry added")


def find_words(search_term: str) -> list[tuple[str, str]]:
    words: list[tuple[str, str]] = []

    with open(dictionary_file) as file:
        for line in file:
            line = line.replace("\n", "")

            fi, en = line.split(";")

            if search_term in fi or search_term in en:
                words.append((fi, en))

    return words


def print_words(words: list[tuple[str, str]]) -> None:
    for word in words:
        fi, en = word

        print(f"{fi} - {en}")


def quit() -> None:
    print("Bye!")


while True:
    print("1 - Add word, 2 - Search, 3 - Quit")

    command = int(input("Function: "))

    if command == 1:
        words = prompt_word()

        add_word(words)
    elif command == 2:
        search_term = input("Search term: ")
        words = find_words(search_term)

        if len(words):
            print_words(words)
        else:
            print("Not found")
    elif command == 3:
        quit()

        break

def search(phonebook: dict[str, list[str]]) -> None:
    name = input("name: ")

    if name not in phonebook:
        print("no number")

        return

    numbers = phonebook[name]

    for number in numbers:
        print(number)


def add(phonebook: dict[str, list[str]]) -> None:
    name = input("name: ")
    number = input("number: ")

    if name not in phonebook:
        phonebook[name] = []

    phonebook[name].append(number)

    print("ok!")


def main() -> None:
    phonebook: dict[str, list[str]] = {}

    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))

        if command == 1:
            search(phonebook)
        elif command == 2:
            add(phonebook)
        elif command == 3:
            break

    print("quitting...")


main()

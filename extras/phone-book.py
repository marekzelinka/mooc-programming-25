class PhoneBook:
    def __init__(self) -> None:
        self.__persons: dict[str, list[str]] = {}

    def add_number(self, name: str, number: str) -> None:
        if name not in self.__persons:
            self.__persons[name] = []

        self.__persons[name].append(number)

    def get_numbers(self, name: str) -> list[str] | None:
        return self.__persons.get(name)

    def all_entries(self) -> dict[str, list[str]]:
        return self.__persons


class FileHandler:
    def __init__(self, filename: str) -> None:
        self.__filename: str = filename

    def load_file(self) -> dict[str, list[str]]:
        names: dict[str, list[str]] = {}

        with open(self.__filename) as file:
            for line in file:
                parts = line.strip().split(";")
                name, *numbers = parts

                names[name] = numbers

        return names

    def save_file(self, phonebook: dict[str, list[str]]) -> None:
        with open(self.__filename, "w") as file:
            for name, numbers in phonebook.items():
                line = [name] + numbers

                file.write(f"{';'.join(line)}\n")


class PhoneBookApp:
    def __init__(self) -> None:
        self.__phonebook: PhoneBook = PhoneBook()
        self.__filehandler: FileHandler = FileHandler("phone-book.txt")

        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def help(self) -> None:
        print("commands:")
        print("0 exit")
        print("1 add entry")
        print("2 search")

    def add_entry(self) -> None:
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self) -> None:
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)

        if not numbers:
            print("number unknown")

            return

        for number in numbers:
            print(number)

    def exit(self) -> None:
        self.__filehandler.save_file(self.__phonebook.all_entries())

    def run(self) -> None:
        self.help()

        while True:
            print("")
            command = input("command: ")

            if command == "0":
                self.exit()

                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            else:
                self.help()


# Code for testing
if __name__ == "__main__":
    # phonebook = PhoneBook()
    # phonebook.add_number("Eric", "02-123456")
    # print(phonebook.get_numbers("Eric"))
    # print(phonebook.get_numbers("Emily"))

    # t = FileHandler("phone-book.txt")
    # print(t.load_file())

    app = PhoneBookApp()
    app.run()

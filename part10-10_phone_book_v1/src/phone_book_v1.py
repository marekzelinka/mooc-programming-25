class PhoneBook:
    def __init__(self):
        self.__persons: dict[str, list[str]] = {}

    def add_number(self, name: str, number: str) -> None:
        if name not in self.__persons:
            # add a new dictionary entry with an empty list for the numbers
            self.__persons[name] = []

        self.__persons[name].append(number)

    def get_numbers(self, name: str) -> list[str] | None:
        return self.__persons.get(name)

    def get_person_name_by_number(self, number: str) -> str | None:
        for name, numbers in self.__persons.items():
            if number in numbers:
                return name

        return None

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


class PhoneBookApplication:
    def __init__(self) -> None:
        self.__phonebook: PhoneBook = PhoneBook()
        self.__filehandler: FileHandler = FileHandler("phonebook.txt")

        # add the names and numbers from the file to the phone book
        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def help(self) -> None:
        print("commands: ")

        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 search by number")

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

    def search_by_number(self) -> None:
        number = input("number: ")

        name = self.__phonebook.get_person_name_by_number(number)

        if not name:
            print("unknown number")

            return

        print(name)

    def exit(self) -> None:
        self.__filehandler.save_file(self.__phonebook.all_entries())

    def execute(self) -> None:
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
            elif command == "3":
                self.search_by_number()
            else:
                self.help()


# when you run the tests, nothing apart from these two lines should be placed in the main function, outside any class definitions
application = PhoneBookApplication()
application.execute()

from typing import Protocol


class Person:
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__numbers: list[str] = []
        self.__address: str | None = None

    @property
    def name(self) -> str:
        return self.__name

    @property
    def numbers(self) -> list[str]:
        return self.__numbers

    @property
    def address(self) -> str | None:
        return self.__address

    def add_number(self, number: str) -> None:
        self.__numbers.append(number)

    def add_address(self, address: str) -> None:
        self.__address = address


class Phonebook:
    def __init__(self) -> None:
        self.__persons: dict[str, Person] = {}

    def add_number(self, name: str, number: str) -> None:
        if name not in self.__persons:
            self.__persons[name] = Person(name)

        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str) -> None:
        if name not in self.__persons:
            self.__persons[name] = Person(name)

        self.__persons[name].add_address(address)

    def get_entry(self, name: str) -> Person | None:
        return self.__persons.get(name)

    def all_entries(self) -> dict[str, Person]:
        return self.__persons


class PhonebookStorageService(Protocol):
    def __init__(self, filename: str) -> None: ...

    def load_file(self) -> dict[str, Person]: ...

    def save_file(self, phonebook: dict[str, Person]) -> None: ...


class PhonebookFileStorage(PhonebookStorageService):
    def __init__(self, filename: str) -> None:
        self.__filename: str = filename

    def load_file(self) -> dict[str, Person]:
        names: dict[str, Person] = {}

        with open(self.__filename) as file:
            for line in file:
                parts = line.strip().split(";")
                name, address, *numbers = parts

                person = Person(name)
                person.add_address(address)

                for number in numbers:
                    person.add_number(number)

                names[name] = person

        return names

    def save_file(self, phonebook: dict[str, Person]) -> None:
        with open(self.__filename, "w") as file:
            for name, person in phonebook.items():
                lines = []
                lines.append(person.name)
                lines.append(person.address or "")

                for number in person.numbers:
                    lines.append(number)

                file.write(f"{';'.join(lines)}\n")


class PhonebookApp:
    def __init__(self, storage_service: PhonebookStorageService) -> None:
        self.__running: bool = False
        self.__phonebook: Phonebook = Phonebook()
        self.__storage_service: PhonebookStorageService = storage_service

        for name, person in self.__storage_service.load_file().items():
            if person.address:
                self.__phonebook.add_address(name, person.address)

            for number in person.numbers:
                self.__phonebook.add_number(name, number)

    def add_number(self, inputs: tuple[str, str]) -> None:
        self.__phonebook.add_number(*inputs)

    def add_address(self, inputs: tuple[str, str]) -> None:
        self.__phonebook.add_address(*inputs)

    def search_by_name(self, inputs: tuple[str]) -> Person | None:
        return self.__phonebook.get_entry(*inputs)

    def help(self) -> None:
        print("Commands:")
        print("0 exit")
        print("1 add number")
        print("2 add address")
        print("3 search by name")

    def exit(self) -> None:
        self.__storage_service.save_file(self.__phonebook.all_entries())

        self.__running = False

        print("\nExiting...")

    def run(self) -> None:
        self.__running = True

        print("Welcome to your phonebook!\n")

        self.help()

        while self.__running:
            print("")

            command = input("Command: ")

            if command == "0":
                self.exit()
            elif command == "1":
                self.add_number(self.__add_number_inputs())
            elif command == "2":
                self.add_address(self.__add_address_inputs())
            elif command == "3":
                person = self.search_by_name(self.__search_inputs())
                self.__print_matches(person)
            else:
                self.help()

    def __add_number_inputs(self):
        name = input("name: ")
        number = input("number: ")

        return name, number

    def __add_address_inputs(self):
        name = input("name: ")
        address = input("address: ")

        return name, address

    def __search_inputs(self):
        name = input("name: ")

        return (name,)

    def __print_matches(self, person: Person | None) -> None:
        if not person:
            print("Person not found")

            return

        if not person.numbers:
            print("Unknown phone numbers")
        else:
            for number in person.numbers:
                print(number)

        if not person.address:
            print("Unknown address")
        else:
            print(f"address: {person.address}")


# Code for testing
if __name__ == "__main__":
    storage_service = PhonebookFileStorage("phonebook.txt")
    app = PhonebookApp(storage_service)
    app.run()

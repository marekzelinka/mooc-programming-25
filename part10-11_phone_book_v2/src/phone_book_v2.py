class Person:
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__numbers: list[str] = []
        self.__addresses: list[str] = []

    def name(self) -> str:
        return self.__name

    def numbers(self) -> list[str]:
        return self.__numbers

    def add_number(self, number: str) -> None:
        self.__numbers.append(number)

    def address(self) -> str | None:
        if not self.__addresses:
            return None

        return self.__addresses[-1]

    def add_address(self, address: str) -> None:
        self.__addresses.append(address)


class PhoneBook:
    def __init__(self):
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


class PhoneBookApplication:
    def __init__(self) -> None:
        self.__phonebook: PhoneBook = PhoneBook()

    def help(self) -> None:
        print("commands: ")

        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self) -> None:
        name = input("name: ")
        number = input("number: ")

        self.__phonebook.add_number(name, number)

    def search(self) -> None:
        name = input("name: ")

        person = self.__phonebook.get_entry(name)

        if not person:
            print("address unknown")
            print("number unknown")

            return

        numbers = person.numbers()

        if not numbers:
            print("number unknown")
        else:
            for number in person.numbers():
                print(number)

        address = person.address()

        if not address:
            print("address unknown")
        else:
            print(f"address: {address}")

    def add_address(self) -> None:
        name = input("name: ")
        address = input("address: ")

        self.__phonebook.add_address(name, address)

    def execute(self) -> None:
        self.help()

        while True:
            print("")

            command = input("command: ")

            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()
# phonebook = PhoneBook()
# phonebook.add_number("Eric", "02-123456")
# phonebook.add_address("Eric", "Linnankatu 75, Turku")
# person = phonebook.get_entry("Eric")
# if person:
#     print(person.name(), person.numbers(), person.address())

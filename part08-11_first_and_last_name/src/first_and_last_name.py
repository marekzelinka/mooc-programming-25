class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def return_first_name(self) -> str:
        return self.name.split(" ")[0]

    def return_last_name(self) -> str:
        return self.name.split(" ")[1]


if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())  # Peter
    print(peter.return_last_name())  # Pythons

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())  # Paula
    print(paula.return_last_name())  # Pythonnen

class Pet:
    def __init__(self, name: str, description: str) -> None:
        self.name: str = name
        self.description: str = description

    def __str__(self) -> str:
        return f"{self.name} ({self.description})"


class Person:
    def __init__(self, name: str, pet: Pet) -> None:
        self.name: str = name
        self.pet: Pet = pet

    def __str__(self) -> str:
        return f"{self.name}, whose pal is {self.pet.name}, a {self.pet.description}"


if __name__ == "__main__":
    hulda = Pet("Hulda", "mixed-breed dog")
    levi = Person("Levi", hulda)

    print(levi)

# Note! Do not change the class Person!
class Person:
    def __init__(self, name: str, age: int, height: int, weight: int) -> None:
        self.name: str = name
        self.age: int = age
        self.height: int = height
        self.weight: int = weight


class BabyCentre:
    def __init__(self) -> None:
        self.number_of_weigh_ins: int = 0

    def weigh(self, person: Person) -> int:
        self.number_of_weigh_ins += 1

        return person.weight

    def feed(self, person: Person) -> None:
        person.weight += 1

    def weigh_ins(self) -> int:
        return self.number_of_weigh_ins

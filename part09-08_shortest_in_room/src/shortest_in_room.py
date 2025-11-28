class Person:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def __str__(self) -> str:
        return self.name


class Room:
    def __init__(self) -> None:
        self.persons: list[Person] = []

    def add(self, person: Person) -> None:
        self.persons.append(person)

    def is_empty(self) -> bool:
        return not self.persons

    def print_contents(self) -> None:
        lines = []

        combined_height = sum(map(lambda person: person.height, self.persons))
        lines.append(
            f"There are {len(self.persons)} persons in the room, and their combined height is {combined_height} cm"
        )

        for person in self.persons:
            lines.append(f"{person.name} ({person.height} cm)")

        print("\n".join(lines))

    def shortest(self) -> Person | None:
        if not self.persons:
            return None

        return min(self.persons, key=lambda person: person.height)

    def remove_shortest(self) -> Person | None:
        shortest = self.shortest()

        if not shortest:
            return None

        self.persons.remove(shortest)

        return shortest


if __name__ == "__main__":
    room = Room()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))

    print()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    print()

    room.print_contents()

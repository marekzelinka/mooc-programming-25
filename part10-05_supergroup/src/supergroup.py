# Write your solution here:
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name: str = name
        self.superpowers: str = superpowers

    def __str__(self):
        return f"{self.name}, superpowers: {self.superpowers}"


class SuperGroup:
    def __init__(self, name: str, location: str) -> None:
        self._name: str = name
        self._location: str = location
        self._members: list[SuperHero] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> str:
        return self._location

    def add_member(self, hero: SuperHero) -> None:
        self._members.append(hero)

    def print_group(self) -> None:
        print(f"{self.name}, {self.location}")
        print("Members:")
        for member in self._members:
            print(member)

class Item:
    """
    Used to model items in a suitcase.

    Each item has a name and weight (in kilograms).
    """

    def __init__(self, name: str, weight: int) -> None:
        self.__name: str = name
        self.__weight: int = weight

    def name(self) -> str:
        """Returns the item name, this should be a property getter, but then the exercise tests would fail."""

        return self.__name

    def weight(self) -> int:
        """Returns the item weight, this should be a property getter, but then the exercise tests would fail."""

        return self.__weight

    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    """
    Used to model a suitcase that has a maximum combined weight for the items stored within.
    """

    def __init__(self, max_weight: int) -> None:
        self.__max_weight: int = max_weight
        self.__items: list[Item] = []

    @property
    def max_weight(self) -> int:
        return self.__max_weight

    def add_item(self, item: Item) -> None:
        """
        Adds a item to the items list.

        Succeeds if the combined weight of all the items, plus of the item we want to add, does not exceed the suitcase max weight.
        """

        if self.__combined_weight_exceeded(item.weight()):
            return

        self.__items.append(item)

    def print_items(self) -> None:
        """Prints out all the items."""

        for item in self.__items:
            print(item)

    def weight(self) -> int:
        """Returns the combined weight of all items."""

        return sum(item.weight() for item in self.__items)

    def heaviest_item(self) -> Item | None:
        """
        Returns the heaviest item that was added earliest.

        Returns `None` if the suitcase is empty.
        """

        if not self.__items:
            return None

        return max(self.__items, key=lambda item: item.weight())

    def __combined_weight_exceeded(self, additional_weight: int) -> bool:
        """Check if the combined weight of all items, plus any additional weight, exceeds the maximum allowed weight."""

        combined_weight = self.weight() + additional_weight

        return combined_weight > self.__max_weight

    def __str__(self) -> str:
        return f"{len(self.__items)} {'item' if len(self.__items) == 1 else 'items'} ({self.weight()} kg)"


class CargoHold:
    """Models a container for suitcases."""

    def __init__(self, max_weight: int) -> None:
        self.__max_weight: int = max_weight
        self.__suitcases: list[Suitcase] = []

    @property
    def max_weight(self) -> int:
        return self.__max_weight

    def add_suitcase(self, suitcase: Suitcase) -> None:
        """
        Adds a suitcase to the suitecases list.

        Succeeds if the combined weight of each suitcase, plus of the suitcase we want to add, does not exceed the cargo holder max weight.
        """

        if self.__combined_weight_exceeded(suitcase.weight()):
            return

        self.__suitcases.append(suitcase)

    def weight(self) -> int:
        """Returns the combined weight of all suitcases."""

        return sum(suitcase.weight() for suitcase in self.__suitcases)

    def print_items(self) -> None:
        """Prints out items for every suitcase."""

        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __combined_weight_exceeded(self, additional_weight: int) -> bool:
        """Check if the combined weight exceeds the maximum allowed weight."""

        combined_weight = self.weight() + additional_weight

        return combined_weight > self.__max_weight

    def __space_left(self) -> int:
        """Returns the space left in the cargo hold, maximum weight, minus the combined weight of all suitcases."""

        return self.__max_weight - self.weight()

    def __str__(self) -> str:
        return f"{len(self.__suitcases)} {'suitcase' if len(self.__suitcases) == 1 else 'suitcases'}, space for {self.__space_left()} kg"


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()

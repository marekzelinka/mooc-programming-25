def sort_by_price(items: list[tuple[str, float]]) -> list[tuple[str, float]]:
    def order_by_price(item: tuple) -> float:
        """Order by price, which is the second item within the tuple."""

        return item[1]

    return sorted(items, key=order_by_price)


if __name__ == "__main__":
    products = [
        ("banana", 5.95),
        ("apple", 3.95),
        ("orange", 4.50),
        ("watermelon", 4.95),
    ]

    for product in sort_by_price(products):
        print(product)


class Student:
    """Models a signle uni student."""

    def __init__(self, name: str, id: str, credits: int) -> None:
        self.name = name
        self.id = id
        self.credits = credits

    def __str__(self) -> str:
        return f"{self.name} ({self.id}), {self.credits} cr."


def by_id(item: Student):
    return item.id


def by_credits(item: Student):
    return item.credits


if __name__ == "__main__":
    o1 = Student("Archie", "a123", 220)
    o2 = Student("Marvin", "m321", 210)
    o3 = Student("Anna", "a999", 131)

    students = [o1, o2, o3]

    print("Sort by id:")
    for student in sorted(students, key=by_id):
        print(student)

    print()

    print("Sort by credits:")
    for student in sorted(students, key=by_credits):
        print(student)

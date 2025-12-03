class Country:
    """Models a single country with population."""

    def __init__(self, name: str, population: int) -> None:
        self.name: str = name
        self.population: int = population


class RunningEvent:
    """Models a food-race event of a length of n meters."""

    def __init__(self, length: int, name: str = "no name") -> None:
        self.length: int = length
        self.name: str = name

    def __repr__(self) -> str:
        return f"{self.length} m. ({self.name})"


class Book:
    def __init__(self, name: str, author: str, page_count: int) -> None:
        self.name: str = name
        self.author: str = author
        self.page_count: int = page_count


class Bookshelf:
    def __init__(self) -> None:
        self._books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def __iter__(self) -> "Bookshelf":
        self.n = 0

        return self

    def __next__(self) -> "Book":
        if self.n >= len(self._books):
            raise StopIteration

        book = self._books[self.n]

        self.n += 1

        return book


if __name__ == "__main__":
    finland = Country("Finland", 6000000)
    malta = Country("Malta", 500000)
    sweden = Country("Sweden", 10000000)
    iceland = Country("Iceland", 350000)

    countries = [finland, malta, sweden, iceland]

    bigger_countries = filter(lambda c: c.population > 5_000_000, countries)

    for country in bigger_countries:
        print(country.name, country.population)

    print()
    print()

    race_lengths = [100, 200, 1500, 3000, 42_195]
    events = [RunningEvent(length) for length in race_lengths]

    # Print out all the events
    print(events)

    # Pick the last one from the list and give it a name
    marathon = events[-1]
    marathon.name = "Marathon"

    # Print out all the events again, including the updated one with a new name
    print(events)

    print()
    print()

    b1 = Book("The Life of Python", "Montague Python", 123)
    b2 = Book("The Old Man and the C", "Ernest Hemingjavay", 204)
    b3 = Book("A Good Cup of Java", "Caffee Coder", 997)
    books = [b1, b2, b3]

    shelf = Bookshelf()

    for book in books:
        shelf.add_book(book)

    # Create a list containing the names of all books
    book_names = [book.name for book in shelf]

    print(book_names)

class Book:
    """Models a simple book"""

    def __init__(self, name: str, author: str) -> None:
        self.name: str = name
        self.author: str = author

    def __str__(self) -> str:
        return f"{self.name} ({self.author})"


class Thesis(Book):
    """Models a graduate thesis"""

    def __init__(self, name: str, author: str, grade: int) -> None:
        super().__init__(name, author)
        self.grade: int = grade


class BookContainer:
    """Models a generic container for books."""

    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def print_books(self) -> None:
        for book in self.books:
            print(book)


class Bookshelf(BookContainer):
    """Models a shelf for books."""

    def __init__(self) -> None:
        super().__init__()

    def add_book(self, book: Book, location: int | None = None) -> None:
        if location is None:
            super().add_book(book)

            return

        self.books.insert(location, book)


if __name__ == "__main__":
    # Create some books for testing
    b1 = Book("Old Man and the Sea", "Ernest Hemingway")
    b2 = Book("Silent Spring", "Rachel Carson")
    b3 = Book("Pride and Prejudice", "Jane Austen")

    thesis = Thesis("Python and the Universe", "Peter Pythons", 3)

    # Print out the values of the attributes
    print(thesis.name)
    print(thesis.author)
    print(thesis.grade)

    print()

    # Create a BookContainer and add the books
    container = BookContainer()
    container.add_book(b1)
    container.add_book(b2)
    container.add_book(b3)

    # Create a Bookshelf and add the books (always to the beginning)
    shelf = Bookshelf()
    shelf.add_book(b1, 0)
    shelf.add_book(b2, 0)
    shelf.add_book(b3, 0)

    # Tulostetaan
    print("Container:")
    container.print_books()

    print()

    print("Shelf:")
    shelf.print_books()

class Book:
    """Models a simple book"""

    def __init__(self, name: str, author: str, page_count: int) -> None:
        self.name: str = name
        self.author: str = author
        self.page_count: int = page_count

    def __str__(self) -> str:
        return f"{self.name} by {self.author} ({self.page_count} {'page' if self.page_count == 1 else 'pages'})"


class Thesis(Book):
    """Models a graduate thesis"""

    def __init__(self, name: str, author: str, page_count: int, grade: int) -> None:
        super().__init__(name, author, page_count)
        self.grade: int = grade


class BookContainer:
    """Models a generic container for books."""

    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def __iter__(self) -> "BookContainer":
        self.iter_counter = 0

        return self

    def __next__(self):
        if self.iter_counter >= len(self.books):
            raise StopIteration

        book = self.books[self.iter_counter]
        self.iter_counter += 1

        return book


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
    b1 = Book("Old Man and the Sea", "Ernest Hemingway", 720)
    b2 = Book("Silent Spring", "Rachel Carson", 640)
    b3 = Book("Pride and Prejudice", "Jane Austen", 425)

    thesis = Thesis("Python and the Universe", "Peter Pythons", 62, 3)

    # Create a Bookshelf and add the books (always to the beginning)
    shelf = Bookshelf()
    shelf.add_book(b1, 0)
    shelf.add_book(b2, 0)
    shelf.add_book(b3, 0)
    shelf.add_book(thesis, 0)

    for book in shelf:
        print(book.name)

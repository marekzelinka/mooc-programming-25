class Notebook:
    """Models notes in a string format."""

    def __init__(self) -> None:
        self._notes: list[str] = []

    def add_note(self, note: str) -> None:
        self._notes.append(note)

    def retrieve_note(self, location: int) -> str:
        return self._notes[location]

    def all_notes(self) -> str:
        return ",".join(self._notes)


class NotebookPro(Notebook):
    """Models a notebook with search functionality."""

    def __init__(self) -> None:
        super().__init__()

    def find_notes(self, search_term: str) -> list[str]:
        return [note for note in self._notes if search_term in note]


if __name__ == "__main__":
    notebook = NotebookPro()
    notebook.add_note("Python is a programming language")
    print(notebook.find_notes("Python"))


# class Notebook:
#     """Models notes in a string format."""

#     def __init__(self) -> None:
#         self.__notes: list[str] = []

#     @property
#     def notes(self) -> list[str]:
#         return self.__notes

#     def add_note(self, note: str) -> None:
#         self.__notes.append(note)

#     def retrieve_note(self, location: int) -> str:
#         return self.__notes[location]

#     def all_notes(self) -> str:
#         return ",".join(self.__notes)


# class NotebookPro(Notebook):
#     """Models a notebook with search functionality."""

#     def __init__(self) -> None:
#         super().__init__()

#     def find_notes(self, search_term: str) -> list[str]:
#         return [note for note in self.notes if search_term in note]


# if __name__ == "__main__":
#     notebook = NotebookPro()
#     notebook.add_note("Python is a programming language")
#     print(notebook.find_notes("Python"))

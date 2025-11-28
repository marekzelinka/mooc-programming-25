class Diary:
    def __init__(self, owner: str) -> None:
        self.__owner: str = owner
        self.__entries: list[str] = []

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str) -> None:
        if not owner.strip():
            raise ValueError("Owner may not be an empty string")

        self.__owner = owner

    def add_entry(self, entry: str) -> None:
        self.__entries.append(entry)

    def print_entries(self) -> None:
        print(f"A total of {len(self.__entries)} entries")

        for entry in self.__entries:
            print(f"- {entry}")


if __name__ == "__main__":
    diary = Diary("Peter")
    diary.add_entry("Today I ate porridge")
    diary.add_entry("Today I learned object oriented programming")
    diary.add_entry("Today I went to bed early")
    diary.print_entries()

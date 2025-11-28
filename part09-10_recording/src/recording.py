class Recording:
    def __init__(self, length: int) -> None:
        if length < 0:
            raise ValueError("Length must not be below 0")

        self.__length: int = length

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int) -> None:
        if length < 0:
            raise ValueError("Length must not be below 0")

        self.__length = length


if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)

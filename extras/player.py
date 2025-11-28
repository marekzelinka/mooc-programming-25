class Player:
    def __init__(self, name: str, tag: int) -> None:
        self.__name: str = name

        if tag <= 0:
            raise ValueError("Player tag must be a positive number")

        self.__tag: int = tag

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if name.strip() == "":
            raise ValueError("Name may not be an empty string")

        self.__name = name

    @property
    def tag(self) -> int:
        return self.__tag

    @tag.setter
    def tag(self, tag: int) -> None:
        if tag <= 0:
            raise ValueError("Player tag must be a positive number")

        self.__tag = tag


if __name__ == "__main__":
    player = Player("Betty Ballmer", 10)
    print(player.name)
    print(player.tag)
    player.name = "a"

    player.name = "Buster Ballmer"
    player.tag = 11
    print(player.name)
    print(player.tag)

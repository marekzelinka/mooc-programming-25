# TEE RATKAISUSI TÄHÄN:
class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int) -> None:
        self.name: str = name
        self.publishe: str = publisher
        self.year: int = year


class GameWarehouse:
    def __init__(self) -> None:
        self.__games: list[ComputerGame] = []

    def add_game(self, game: ComputerGame) -> None:
        self.__games.append(game)

    def list_games(self) -> list[ComputerGame]:
        return self.__games


class GameMuseum(GameWarehouse):
    def __init__(self) -> None:
        super().__init__()

    def list_games(self) -> list[ComputerGame]:
        return [game for game in super().list_games() if game.year < 1990]


if __name__ == "__main__":
    museum = GameMuseum()
    museum.add_game(ComputerGame("Pacman", "Namco", 1980))
    museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
    museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))
    for game in museum.list_games():
        print(game.name)

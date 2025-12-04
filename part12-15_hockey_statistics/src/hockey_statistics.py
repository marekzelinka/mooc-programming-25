# Write your solution here
import json


class Player:
    def __init__(
        self,
        name: str,
        nationality: str,
        assists: int,
        goals: int,
        penalties: int,
        team: str,
        games: int,
    ) -> None:
        self.name: str = name
        self.nationality: str = nationality
        self.assists: int = assists
        self.goals: int = goals
        self.penalties: int = penalties
        self.team: str = team
        self.games: int = games

    def __str__(self) -> str:
        return f"{self.name:21}{self.team}  {self.goals:>2} + {self.assists:>2} = {self.points:>3}"

    @property
    def points(self) -> int:
        return self.goals + self.assists


class HockeyStatistics:
    def __init__(self) -> None:
        self.__players: dict[str, Player] = {}

    def add_player(
        self,
        name: str,
        nationality: str,
        assists: int,
        goals: int,
        penalties: int,
        team: str,
        games: int,
    ) -> None:
        self.__players[name] = Player(
            name,
            nationality,
            assists,
            goals,
            penalties,
            team,
            games,
        )

    def get_player(self, name: str) -> Player | None:
        return self.__players.get(name)

    def all_teams(self) -> list[str]:
        return sorted(
            list(set(map(lambda player: player.team, self.__players.values())))
        )

    def all_countries(self) -> list[str]:
        return sorted(
            list(set(map(lambda player: player.nationality, self.__players.values())))
        )

    def filter_by_team(self, team: str) -> list[Player]:
        return sorted(
            filter(lambda player: player.team == team, self.__players.values()),
            key=lambda player: player.points,
            reverse=True,
        )

    def filter_by_nationality(self, nationality: str) -> list[Player]:
        return sorted(
            filter(
                lambda player: player.nationality == nationality,
                self.__players.values(),
            ),
            key=lambda player: player.points,
            reverse=True,
        )

    def filter_by_most_point(self, count: int) -> list[Player]:
        return sorted(
            self.__players.values(),
            key=lambda player: (player.points, player.goals),
            reverse=True,
        )[:count]

    def filter_by_most_goals(self, count: int) -> list[Player]:
        return sorted(
            self.__players.values(),
            key=lambda player: (player.goals, -player.games),
            reverse=True,
        )[:count]

    @property
    def players(self) -> dict[str, Player]:
        return self.__players


class HockeyStatisticsApplication:
    def __init__(self) -> None:
        self.__running: bool = False
        self.__filename: str | None = None
        self.__stats: HockeyStatistics = HockeyStatistics()

    def search(self) -> None:
        name = input("name: ")
        print()

        player = self.__stats.get_player(name)

        if not player:
            print("player not found")

            return

        print(player)

    def teams(self) -> None:
        team_list = self.__stats.all_teams()

        for team in team_list:
            print(team)

    def countries(self) -> None:
        country_list = self.__stats.all_countries()

        for country in country_list:
            print(country)

    def team_players(self) -> None:
        team = input("team: ")
        print()

        players = self.__stats.filter_by_team(team)

        if not players:
            print("no players found")

        for player in players:
            print(player)

    def players_from_country(self) -> None:
        nationality = input("country: ")
        print()

        players = self.__stats.filter_by_nationality(nationality)

        if not players:
            print("no players found")
        for player in players:
            print(player)

    def most_points(self) -> None:
        count = int(input("how many: "))
        print()

        players = self.__stats.filter_by_most_point(count)

        if not players:
            print("no players found")

        for player in players:
            print(player)

    def most_goals(self) -> None:
        count = int(input("how many: "))
        print()

        players = self.__stats.filter_by_most_goals(count)

        if not players:
            print("no players found")

        for player in players:
            print(player)

    def run(self) -> None:
        self.__running = True

        filename = input("file name: ")

        self.__load_players(filename)

        print(f"read the data of {len(self.__stats.players.values())} players")

        print()

        self.__help()

        while self.__running:
            print()

            command = input("command: ")

            if command == "0":
                self.__exit()
            elif command == "1":
                self.search()
            elif command == "2":
                self.teams()
            elif command == "3":
                self.countries()
            elif command == "4":
                self.team_players()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
            else:
                self.__help()

    def __help(self) -> None:
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def __exit(self) -> None:
        self.__running = False

    def __load_players(self, filename: str) -> None:
        self.__filename = filename

        with open(filename) as file:
            data = file.read()

        players = json.loads(data)

        for player in players:
            self.__stats.add_player(**player)


app = HockeyStatisticsApplication()
app.run()

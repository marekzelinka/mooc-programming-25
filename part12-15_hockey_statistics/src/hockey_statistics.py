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
        return f"{self.name:20} {self.team}  {self.goals:2} + {self.assists:2} = {self.points:3}"

    @property
    def points(self) -> int:
        return self.goals + self.assists


class HockeyStatistics:
    def __init__(self) -> None:
        self.__players: dict[str, Player] = {}

    @property
    def players(self) -> dict[str, Player]:
        return self.__players

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

    def teams(self) -> list[str]:
        return sorted(
            list(set(map(lambda player: player.team, self.__players.values())))
        )

    def countries(self) -> list[str]:
        return sorted(
            list(set(map(lambda player: player.nationality, self.__players.values())))
        )

    def filter_players_by_team(self, team: str) -> list[Player]:
        players = filter(lambda player: player.team == team, self.__players.values())

        return sorted(
            players,
            key=self.__filter_by_most_points,
            reverse=True,
        )

    def filter_players_by_country(self, country: str) -> list[Player]:
        players = filter(
            lambda player: player.nationality == country,
            self.__players.values(),
        )

        return sorted(
            players,
            key=self.__filter_by_most_points,
            reverse=True,
        )

    def filter_players_by_most_points(self, limit: int) -> list[Player]:
        return sorted(
            self.__players.values(),
            key=self.__filter_by_most_points,
            reverse=True,
        )[:limit]

    def filter_players_by_most_goals(self, limit: int) -> list[Player]:
        return sorted(
            self.__players.values(),
            key=self.__filter_by_most_goals,
            reverse=True,
        )[:limit]

    def __filter_by_most_points(self, player: Player) -> int:
        return player.points

    def __filter_by_most_goals(self, player: Player) -> tuple[int, int]:
        return (player.goals, -player.games)


class HockeyStatisticsApplication:
    def __init__(self) -> None:
        self.__running: bool = False
        self.__filename: str | None = None
        self.__stats: HockeyStatistics = HockeyStatistics()

    def search_player_by_name(self) -> None:
        name = input("name: ")

        player = self.__stats.get_player(name)

        if not player:
            return

        print(player)

    def get_teams(self) -> None:
        teams = self.__stats.teams()

        for team in teams:
            print(team)

    def get_countries(self) -> None:
        countries = self.__stats.countries()

        for country in countries:
            print(country)

    def search_players_by_team(self) -> None:
        team = input("team: ")

        players_in_team = self.__stats.filter_players_by_team(team)

        if not players_in_team:
            return

        for player in players_in_team:
            print(player)

    def search_players_by_countr(self) -> None:
        country = input("country: ")

        players_by_country = self.__stats.filter_players_by_country(country)

        if not players_by_country:
            return

        for player in players_by_country:
            print(player)

    def get_players_with_most_points(self) -> None:
        limit = int(input("how many: "))

        players_by_most_points = self.__stats.filter_players_by_most_points(limit)

        if not players_by_most_points:
            return

        for player in players_by_most_points:
            print(player)

    def get_players_with_most_goals(self) -> None:
        limit = int(input("how many: "))

        players_by_most_goals = self.__stats.filter_players_by_most_goals(limit)

        if not players_by_most_goals:
            return

        for player in players_by_most_goals:
            print(player)

    def run(self) -> None:
        self.__running = True

        self.__load_players()

        self.__help()

        while self.__running:
            print()

            command = input("command: ")

            if command == "0":
                self.__exit()
            elif command == "1":
                self.search_player_by_name()
            elif command == "2":
                self.get_teams()
            elif command == "3":
                self.get_countries()
            elif command == "4":
                self.search_players_by_team()
            elif command == "5":
                self.search_players_by_countr()
            elif command == "6":
                self.get_players_with_most_points()
            elif command == "7":
                self.get_players_with_most_goals()
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

    def __load_players(self) -> None:
        filename = input("file name: ")

        self.__filename = filename

        with open(filename) as file:
            data = file.read()

        players = json.loads(data)

        for player in players:
            self.__stats.add_player(**player)

        print(f"read the data of {len(self.__stats.players.values())} players")


app = HockeyStatisticsApplication()
app.run()

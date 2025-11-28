class WeatherStation:
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__observations: list[str] = []

    def add_observation(self, description: str) -> None:
        self.__observations.append(description)

    def latest_observation(self) -> str:
        if not self.__observations:
            return ""

        return self.__observations[-1]

    def number_of_observations(self) -> int:
        return len(self.__observations)

    def __str__(self) -> str:
        return f"{self.__name}, {len(self.__observations)} observations"


if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)

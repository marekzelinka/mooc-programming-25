from math import sqrt

from .types import Coordinates, LocationDistance


def get_station_data(filename: str) -> dict[str, Coordinates]:
    stations: dict[str, Coordinates] = {}

    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")

            parts = line.split(";")

            if parts[0] == "Longitude":
                # Ignore csv header
                continue

            print(f"{parts=}")

            longitude = float(parts[0])
            latitude = float(parts[1])
            _fid = parts[2]
            name = parts[3]

            stations[name] = (longitude, latitude)

    return stations


def distance_km(a: Coordinates, b: Coordinates) -> float:
    x_km = (a[0] - b[0]) * 55.26
    y_km = (a[1] - b[1]) * 111.2

    return sqrt(x_km**2 + y_km**2)


def distance(stations: dict[str, Coordinates], station1: str, station2: str) -> float:
    a = stations[station1]
    b = stations[station2]

    return distance_km(a, b)


def greatest_distance(stations: dict[str, Coordinates]) -> LocationDistance:
    result: tuple[str, str, float] = "", "", 0

    for a in stations:
        for b in stations:
            station_distance = distance(stations, a, b)

            if station_distance > result[2]:
                result = (a, b, station_distance)

    return result

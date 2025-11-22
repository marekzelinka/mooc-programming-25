from .types import Movie


def add_movie(db: list[Movie], name: str, director: str, year: int, runtime: int):
    movie: Movie = {
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime,
    }

    db.append(movie)


def main() -> None:
    database: list[Movie] = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(
        database
    )  # [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]


if __name__ == "__main__":
    main()

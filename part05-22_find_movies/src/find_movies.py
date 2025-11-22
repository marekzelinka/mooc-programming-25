from .types import Database


def find_movies(db: Database, search_term: str) -> Database:
    matches: Database = []

    for movie in db:
        if search_term.lower() in movie["name"].lower():
            matches.append(movie)

    return matches


def main() -> None:
    database: Database = [
        {
            "name": "Gone with the Python",
            "director": "Victor Pything",
            "year": 2017,
            "runtime": 116,
        },
        {
            "name": "Pythons on a Plane",
            "director": "Renny Pytholin",
            "year": 2001,
            "runtime": 94,
        },
        {
            "name": "Dawn of the Dead Programmers",
            "director": "M. Night Python",
            "year": 2011,
            "runtime": 101,
        },
    ]

    my_movies = find_movies(database, "python")
    print(my_movies)


if __name__ == "__main__":
    main()

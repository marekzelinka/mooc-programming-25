from typing import TypedDict


class Movie(TypedDict):
    name: str
    director: str
    year: int
    runtime: int


type Database = list[Movie]

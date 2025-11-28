class Series:
    def __init__(self, title: str, seasons: int, genres: list[str]) -> None:
        self.title = title
        self.seasons = seasons
        self.geners = genres
        self.ratings = []

    def __str__(self) -> str:
        lines: list[str] = []

        lines.append(f"{self.title} ({self.seasons} seasons)")
        lines.append(f"genres: {', '.join(self.geners)}")

        if len(self.ratings):
            lines.append(f"{len(self.ratings)} ratings, average {self.rating()} points")
        else:
            lines.append("no ratings")

        return "\n".join(lines)

    def rating(self):
        if not len(self.ratings):
            return 0

        return round(sum(rating for rating in self.ratings) / len(self.ratings), 1)

    def rate(self, rating: int) -> None:
        self.ratings.append(rating)


def minimum_grade(rating: float, series_list: list[Series]) -> list[Series]:
    return [series for series in series_list if series.rating() >= rating]


def includes_genre(genre: str, series_list: list[Series]) -> list[Series]:
    return [series for series in series_list if genre in series.geners]


if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)

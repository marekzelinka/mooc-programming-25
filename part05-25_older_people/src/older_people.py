def older_people(people: list[tuple[str, int]], born_before_year: int) -> list[str]:
    names = []

    for name, year in people:
        if year < born_before_year:
            names.append(name)

    return names


def main() -> None:
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)
    print(older)  # [ 'Adam', 'Mary' ]


if __name__ == "__main__":
    main()

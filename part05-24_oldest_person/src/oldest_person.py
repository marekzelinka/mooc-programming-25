def oldest_person(people: list[tuple[str, int]]) -> str:
    (name, *_rest) = min(people, key=lambda person: person[1])

    return name


def main() -> None:
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))  # Mary


if __name__ == "__main__":
    main()

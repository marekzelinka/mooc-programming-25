def read_fruits() -> dict[str, float]:
    fruits: dict[str, float] = {}

    with open("fruits.csv") as file:
        for line in file:
            line = line.replace("\n", "")

            parts = line.split(";")
            name = parts[0]
            price = float(parts[1])

            fruits[name] = price

    return fruits


def main() -> None:
    fruits = read_fruits()

    print(fruits)


if __name__ == "__main__":
    main()

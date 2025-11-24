def create_tuple(x: int, y: int, z: int):
    it = [x, y, z]

    smallest = min(it)
    largest = max(it)
    total = sum(it)

    return smallest, largest, total


def main() -> None:
    print(create_tuple(5, 3, -1))  # (-1, 5, 7)


if __name__ == "__main__":
    main()

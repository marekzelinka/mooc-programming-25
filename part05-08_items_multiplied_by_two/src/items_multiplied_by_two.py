def double_items(numbers: list[int]) -> list[int]:
    doubled: list[int] = []

    for number in numbers:
        doubled.append(number * 2)

    return doubled


def main() -> None:
    numbers = [2, 4, 5, 3, 11, -4]

    numbers_doubled = double_items(numbers)

    print("original:", numbers)
    print("doubled:", numbers_doubled)


if __name__ == "__main__":
    main()

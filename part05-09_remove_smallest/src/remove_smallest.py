def remove_smallest(numbers: list[int]) -> None:
    smallest = min(numbers)

    numbers.remove(smallest)


def main() -> None:
    numbers: list[int] = [2, 2, 6, 1, 3, 5]

    remove_smallest(numbers)

    print(numbers)  # [2, 4, 6, 3, 5]


if __name__ == "__main__":
    main()

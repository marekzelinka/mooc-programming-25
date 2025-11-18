def list_of_stars(numbers: list[int]) -> None:
    for number in numbers:
        print("*" * number)


if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])

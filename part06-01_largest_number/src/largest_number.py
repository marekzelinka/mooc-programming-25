def largest() -> int:
    numbers: list[int] = []

    with open("./numbers.txt") as file:
        for line in file:
            line = line.replace("\n", "")

            number = int(line)
            numbers.append(number)

    largest_number = max(numbers)

    return largest_number


def main() -> None:
    largest_number = largest()
    print(largest_number)


if __name__ == "__main__":
    main()

def line(width: int, string: str) -> None:
    if len(string) == 0:
        print("*" * width)
    else:
        print(string[0] * width)


def square_of_hashes(size: int):
    i = 0

    while i < size:
        line(size, "#")

        i += 1


if __name__ == "__main__":
    square_of_hashes(5)

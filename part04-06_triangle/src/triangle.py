def line(width: int, string: str) -> None:
    if len(string) == 0:
        print("*" * width)
    else:
        print(string[0] * width)


def triangle(size: int) -> None:
    i = 1

    while i <= size:
        line(i, "#")

        i += 1


if __name__ == "__main__":
    triangle(5)

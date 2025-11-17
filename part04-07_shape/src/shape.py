def line(width: int, char: str) -> None:
    if len(char) == 0:
        print("*" * width)
    else:
        print(char[0] * width)


def triangle(size: int, char: str) -> None:
    i = 1

    while i <= size:
        line(i, char)

        i += 1


def square(width: int, height: int, char: str) -> None:
    while height > 0:
        line(width, char)

        height -= 1


def shape(width: int, triangle_char: str, rect_height: int, rect_char: str) -> None:
    triangle(width, triangle_char)
    square(width, rect_height, rect_char)


if __name__ == "__main__":
    shape(5, "x", 2, "o")

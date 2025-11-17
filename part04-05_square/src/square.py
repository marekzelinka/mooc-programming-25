def line(width: int, string: str) -> None:
    if len(string) == 0:
        print("*" * width)
    else:
        print(string[0] * width)


def square(size: int, character: str) -> None:
    i = 0

    while i < size:
        line(size, character)

        i += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")

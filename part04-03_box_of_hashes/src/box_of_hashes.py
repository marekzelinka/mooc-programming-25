def line(width: int, string: str) -> None:
    if len(string) == 0:
        print("*" * width)
    else:
        print(string[0] * width)


def box_of_hashes(height: int) -> None:
    while height > 0:
        line(10, "#")

        height -= 1


if __name__ == "__main__":
    box_of_hashes(5)

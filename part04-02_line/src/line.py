def line(count: int, char: str) -> None:
    if len(char) == 0:
        print("*" * count)
    else:
        print(char[0] * count)


if __name__ == "__main__":
    line(5, "x")

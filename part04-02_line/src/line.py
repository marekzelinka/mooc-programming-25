def line(width: int, string: str) -> None:
    if len(string) == 0:
        print("*" * width)
    else:
        print(string[0] * width)


if __name__ == "__main__":
    line(5, "x")

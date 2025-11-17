def squared(text: str, size: int) -> None:
    col = 0
    string = text

    while col < size:
        while len(string) < size:
            string += text

        print(string[:size])

        string = string[size:]
        col += 1


if __name__ == "__main__":
    squared("ab", 3)

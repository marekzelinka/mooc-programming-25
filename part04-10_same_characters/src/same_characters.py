def same_chars(string: str, first: int, second: int) -> bool:
    if first >= len(string) or second >= len(string):
        return False

    return string[first] == string[second]


if __name__ == "__main__":
    print(same_chars("coder", 1, 2))

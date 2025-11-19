def longest(strings: list[str]) -> str:
    longest_string = strings[0]

    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string

    return longest_string


def main() -> None:
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]

    print(longest(strings))


if __name__ == "__main__":
    main()

def invert(dictionary: dict):
    inverted = {}

    for value, key in dictionary.items():
        inverted[key] = value

    dictionary.clear()

    for key, value in inverted.items():
        dictionary[key] = value


def main() -> None:
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)  # {"first": 1, "second": 2, "third": 3, "fourth": 4}


if __name__ == "__main__":
    main()

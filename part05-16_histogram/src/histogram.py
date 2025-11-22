def histogram(word: str) -> None:
    char_frequencies = {}

    for char in word:
        if char not in char_frequencies:
            char_frequencies[char] = 0

        char_frequencies[char] += 1

    for char, frequency in char_frequencies.items():
        stars = "*" * frequency

        print(f"{char} {stars}")


def main() -> None:
    histogram("abba")
    # a **
    # b **
    histogram("statistically")
    # s **
    # t ***
    # a **
    # i **
    # c *
    # l **
    # y *


if __name__ == "__main__":
    main()

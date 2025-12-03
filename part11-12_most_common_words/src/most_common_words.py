# WRITE YOUR SOLUTION HERE:
from string import punctuation


def most_common_words(filename: str, lower_limit: int) -> dict[str, int]:
    with open(filename) as file:
        contents = file.read()

        # Remove newline char
        contents = contents.replace("\n", " ")

        # Cleanup any punctuations
        for punctuation_mark in punctuation:
            contents = contents.replace(punctuation_mark, "")

        words = contents.split(" ")

        return {
            word: words.count(word)
            for word in words
            if words.count(word) >= lower_limit
        }


if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))

from random import sample


def words(n: int, beginning: str) -> list[str]:
    words: list[str] = []

    with open("words.txt") as file:
        for line in file:
            line = line.replace("\n", "")

            word = line.strip()
            words.append(word)

    filtered = [word for word in set(words) if word.startswith(beginning)]

    return sample(filtered, n)

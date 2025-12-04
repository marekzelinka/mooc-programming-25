# Write your solution here:
from random import sample


def word_generator(characters: str, length: int, amount: int):
    return ("".join(sample(characters, length)) for i in range(amount))


if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)

    for word in wordgen:
        print(word)

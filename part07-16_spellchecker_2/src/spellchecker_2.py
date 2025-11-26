from difflib import get_close_matches
from functools import cache

text = input("write text: ")

words: list[str] = []

with open("wordlist.txt") as file:
    for word in file:
        words.append(word.strip())

misspellings = []

for word in text.split(" "):
    if word.lower() not in words:
        print(f"*{word}*", end=" ")

        if word not in misspellings:
            misspellings.append(word)

        continue

    print(word, end=" ")

print()


@cache
def get_suggestions(word: str) -> list[str]:
    return get_close_matches(word, words)


if len(misspellings):
    print("suggestions:")

    for word in misspellings:
        suggestions = get_suggestions(word)

        print(f"{word}: {', '.join(suggestions)}")

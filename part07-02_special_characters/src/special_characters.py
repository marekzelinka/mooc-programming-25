import string


def separate_characters(my_string: str) -> tuple[str, str, str]:
    letters = ""
    punctuations = ""
    other = ""

    for i in range(len(my_string)):
        char = my_string[i]
        if char in string.ascii_letters:
            letters += char
        elif char in string.punctuation:
            punctuations += char
        else:
            other += char

    return letters, punctuations, other

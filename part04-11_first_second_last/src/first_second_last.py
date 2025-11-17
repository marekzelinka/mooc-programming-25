def first_word(string: str) -> str:
    next_space_index = string.find(" ")

    return string[:next_space_index]


def second_word(string: str) -> str:
    first_space_index = string.find(" ")
    string = string[first_space_index + 1 :]
    next_space_index = string.find(" ")
    if next_space_index == -1:
        return string

    return string[:next_space_index]


def last_word(string: str) -> str:
    last_space = string.rfind(" ")

    return string[last_space + 1 :]


if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))

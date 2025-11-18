def most_common_character(string: str) -> str:
    most_occurring = string[0]

    for char in string:
        occurrences = string.count(char)

        if occurrences > string.count(most_occurring):
            most_occurring = char

    return most_occurring


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))  # b

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))  # e

from typing import List


def length_of_longest(strings: List[str]) -> int:
    longest = strings[0]

    for string in strings[1:]:
        if len(string) > len(longest):
            longest = string

    return len(longest)


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)

from typing import List


def shortest(strings: List[str]) -> str:
    candidate = strings[0]

    for string in strings[1:]:
        if len(string) < len(candidate):
            candidate = string

    return candidate


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)

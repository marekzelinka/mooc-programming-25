def all_the_longest(strings: list[str]) -> list[str]:
    longest: list[str] = []

    for string in strings:
        if longest == [] or len(string) > len(longest[0]):
            longest = [string]
        elif len(string) == len(longest[0]):
            longest.append(string)

    return longest


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result)  # ['eleventh']

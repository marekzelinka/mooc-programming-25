def no_shouting(items: list[str]) -> list[str]:
    result: list[str] = []

    for item in items:
        if not item.isupper():
            result.append(item)

    return result


if __name__ == "__main__":
    my_list = [
        "ABC",
        "def",
        "UPPER",
        "ANOTHERUPPER",
        "lower",
        "another lower",
        "Capitalized",
    ]

    pruned_list = no_shouting(my_list)

    print(pruned_list)  # ['def', 'lower', 'another lower', 'Capitalized']

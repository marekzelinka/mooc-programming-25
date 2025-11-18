def everything_reversed(strings: list[str]) -> list[str]:
    updated: list[str] = []

    for string in strings:
        updated.append(string[::-1])

    return updated[::-1]


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)

    print(new_list)  # ['erom eno', 'elpmaxe', 'ereht', 'iH']

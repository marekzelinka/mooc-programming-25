def no_vowels(string: str) -> str:
    vowels = "aeiou"

    result = ""

    for letter in string:
        if letter not in vowels:
            result += letter

    return result


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))  # ths s n xmpl

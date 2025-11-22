def dict_of_numbers():
    singles = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    whole_tens = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }

    numbers = {}

    # 0 - 9
    for i in range(10):
        numbers[i] = singles[i]

    # 10 - 19 are special cases
    numbers[10] = "ten"
    numbers[11] = "eleven"
    numbers[12] = "twelve"
    numbers[13] = "thirteen"
    numbers[14] = "fourteen"
    numbers[15] = "fifteen"
    numbers[16] = "sixteen"
    numbers[17] = "seventeen"
    numbers[18] = "eighteen"
    numbers[19] = "nineteen"

    # 20 - 99
    for i in range(2, 10):
        numbers[i * 10] = whole_tens[i]
        for j in range(1, 10):
            numbers[i * 10 + j] = whole_tens[i] + "-" + singles[j]

    return numbers


def main() -> None:
    numbers = dict_of_numbers()
    print(numbers[2])  # two
    print(numbers[11])  # eleven
    print(numbers[45])  # forty-five
    print(numbers[99])  # ninety-nine
    print(numbers[0])  # zero


if __name__ == "__main__":
    main()

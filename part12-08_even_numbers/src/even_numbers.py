# Write your solution here
def even_numbers(beginning: int, maximum: int):
    if beginning % 2 != 0:
        beginning += 1

    value = beginning

    while value <= maximum:
        yield value

        value += 2


if __name__ == "__main__":
    numbers = even_numbers(2, 10)

    for number in numbers:
        print(number)

    numbers2 = even_numbers(11, 21)

    for number in numbers2:
        print(number)

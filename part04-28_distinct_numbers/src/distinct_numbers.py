def distinct_numbers(numbers: list[int]) -> list[int]:
    new: list[int] = []

    for number in numbers:
        if number not in new:
            new.append(number)

    new.sort()

    return new


if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))  # [1, 2, 3]

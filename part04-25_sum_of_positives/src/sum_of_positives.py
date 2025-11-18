def sum_of_positives(numbers: list[int]) -> int:
    sum = 0

    for number in numbers:
        if number > 0:
            sum += number

    return sum


if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)

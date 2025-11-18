def mean(numbers: list[int]) -> float:
    total = sum(numbers)

    return total / len(numbers)


if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)

    print(result)

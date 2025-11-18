def range_of_list(numbers: list[int]) -> int:
    ordered = sorted(numbers)
    first = ordered[0]
    last = ordered[-1]

    return last - first


if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)

    print(result)

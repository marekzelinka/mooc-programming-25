from typing import List


def sum_of_positives(list: List[int]) -> int:
    sum = 0

    for n in list:
        if n > 0:
            sum += n

    return sum


if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)

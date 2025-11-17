from typing import List


def distinct_numbers(numbers: List[int]) -> List[int]:
    new: List[int] = []

    for n in numbers:
        if n not in new:
            new.append(n)

    new.sort()

    return new


if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))  # [1, 2, 3]

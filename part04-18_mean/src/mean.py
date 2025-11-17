from typing import List


def mean(list: List[int]) -> float:
    total = sum(list)

    return total / len(list)


if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)

    print(result)

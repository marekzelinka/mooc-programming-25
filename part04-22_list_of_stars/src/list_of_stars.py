from typing import List


def list_of_stars(list: List[int]) -> None:
    for i in list:
        print("*" * i)


if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])

from typing import List


def even_numbers(numbers: List[int]) -> List[int]:
    new: List[int] = []

    for n in numbers:
        if n % 2 == 0:
            new.append(n)

    return new


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)

    print("original", my_list)
    print("new", new_list)

from typing import List


def list_sum(first: List[int], second: List[int]) -> List[int]:
    """
    Takes two lists of integers as arguments and returns a new list which contains the sums of the items at each index in the two original lists.
    """
    new: List[int] = []

    # Another solution would be use zip-function,
    # which creates new list by combining items in two or more lists
    # for item1, item2 in zip(list1, list2):
    #   results.append(item1 + item2)
    # Write your solution here
    for i in range(len(first)):
        a = first[i]
        b = second[i]

        new.append(a + b)

    return new


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]

    print(list_sum(a, b))  # [8, 10, 12]

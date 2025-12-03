from typing import TypeVar

T = TypeVar("T", int, str)


def binary_search(target: list[T], item: T, left: int, right: int) -> bool:
    """
    Returns `True` if the item is contained in the target list, `False` otherwise.

    Support both a list of `int` or `str`.

    The target list must be sorted in ascending order.
    """

    # If the search area is empty, the item was not found
    if left > right:
        return False

    # Calculate the center of the search area, rounded down to nearest int
    center = (left + right) // 2

    # If the item is found at the center, return
    if target[center] == item:
        return True

    if target[center] < item:
        # If the item is greater, search the greater half

        return binary_search(target, item, center + 1, right)
    else:
        # If the item is smaller, search the smaller half

        return binary_search(target, item, left, center - 1)


if __name__ == "__main__":
    # Test your function
    target = [1, 2, 4, 5, 7, 8, 11, 13, 14, 18]

    print(binary_search(target, 2, 0, len(target) - 1))
    print(binary_search(target, 13, 0, len(target) - 1))
    print(binary_search(target, 6, 0, len(target) - 1))
    print(binary_search(target, 15, 0, len(target) - 1))

    print()
    print()

    target2 = ["a", "b", "d", "e", "g", "h", "i", "l", "m"]

    print(binary_search(target2, "e", 0, len(target2) - 1))
    print(binary_search(target2, "h", 0, len(target2) - 1))
    print(binary_search(target2, "f", 0, len(target2) - 1))
    print(binary_search(target2, "d", 0, len(target2) - 1))

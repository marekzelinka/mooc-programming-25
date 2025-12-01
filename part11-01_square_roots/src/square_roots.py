import math


def square_roots(numbers: list[int]) -> list[float]:
    return [math.sqrt(number) for number in numbers]


if __name__ == "__main__":
    lines = square_roots([1, 2, 3, 4])
    for line in lines:
        print(line)

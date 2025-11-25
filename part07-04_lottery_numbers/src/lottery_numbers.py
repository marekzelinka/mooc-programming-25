from random import sample


def lottery_numbers(amount: int, lower: int, upper: int) -> list[int]:
    pool = list(range(lower, upper + 1))
    numbers = sample(pool, amount)

    return sorted(numbers)

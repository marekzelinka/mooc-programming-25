from random import choice


def roll(die: str) -> int:
    dies = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4],
    }

    selected = dies.get(die)

    if not selected:
        raise ValueError('Die must be "A", "B", or "C"')

    return choice(dies[die])


def play(die1: str, die2: str, times: int) -> tuple[int, int, int]:
    die1_wins = 0
    die2_wins = 0
    ties = 0

    for i in range(times):
        die1_roll = roll(die1)
        die2_roll = roll(die2)

        if die1_roll > die2_roll:
            die1_wins += 1
        elif die2_roll > die1_roll:
            die2_wins += 1
        else:
            ties += 1

    return die1_wins, die2_wins, ties

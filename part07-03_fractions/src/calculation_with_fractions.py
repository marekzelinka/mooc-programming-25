from fractions import Fraction


def fractionate(amount: int) -> list[Fraction]:
    return [Fraction(1, amount)] * amount

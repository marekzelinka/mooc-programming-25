# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    DAYS_IN_MONTH = 30
    MONTHS_IN_YEAR = 12
    DAYS_IN_YEAR = MONTHS_IN_YEAR * DAYS_IN_MONTH

    def __init__(self, day: int, month: int, year: int) -> None:
        self.day: int = day
        self.month: int = month
        self.year: int = year

    def __string_helper(self) -> str:
        return f"{self.day}.{self.month}.{self.year}"

    def __str__(self):
        return f"{self.__string_helper()}"

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, SimpleDate):
            return False

        return self.__str__() == value.__str__()

    def __ne__(self, value: object, /) -> bool:
        if not isinstance(value, SimpleDate):
            return False

        return not self.__eq__(value)

    def __gt__(self, another: "SimpleDate") -> bool:
        if self.year != another.year:
            return self.year > another.year
        elif self.month != another.month:
            return self.month > another.month
        else:
            return self.day > another.day

    def __lt__(self, another: "SimpleDate") -> bool:
        greater = self > another

        return not greater

    def __add__(self, another: int) -> "SimpleDate":
        day = self.day + another
        month = self.month
        year = self.year

        if day > self.DAYS_IN_MONTH:
            month += day // self.DAYS_IN_MONTH
            day = day % self.DAYS_IN_MONTH

            if month > self.MONTHS_IN_YEAR:
                year += month // self.MONTHS_IN_YEAR
                month %= self.MONTHS_IN_YEAR

        return SimpleDate(day, month, year)

    def __sub__(self, another: "SimpleDate") -> int:
        if self > another:
            diff_years = self.year - another.year
            diff_months = self.month - another.month
            diff_days = self.day - another.day
        elif self < another:
            diff_years = another.year - self.year
            diff_months = another.month - self.month
            diff_days = another.day - self.day
        else:
            return 0

        return (
            diff_days
            + diff_months * self.DAYS_IN_MONTH
            + diff_years * self.DAYS_IN_YEAR
        )


if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2 - d1)
    print(d1 - d2)
    print(d1 - d3)

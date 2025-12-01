# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __string_helper(self) -> str:
        return f"{self.__euros}.{self.__cents:02d}"

    def __str__(self):
        return f"{self.__string_helper()} eur"

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Money):
            return False

        return self.__string_helper() == value.__string_helper()

    def __ne__(self, value: object, /) -> bool:
        if not isinstance(value, Money):
            return False

        return self.__string_helper() != value.__string_helper()

    def __gt__(self, another: "Money") -> bool:
        return self.__string_helper() > another.__string_helper()

    def __lt__(self, another: "Money") -> bool:
        return self.__string_helper() < another.__string_helper()

    def __add__(self, another: "Money") -> "Money":
        euros = self.__euros + another.__euros
        cents = self.__cents + another.__cents

        if cents >= 100:
            euros += 1
            cents -= 100

        return Money(euros, cents)

    def __sub__(self, another: "Money") -> "Money":
        if self.__cents < another.__cents:
            self.__euros -= 1
            self.__cents += 100

        euros = self.__euros - another.__euros
        cents = self.__cents - another.__cents

        if euros < 0 or cents < 0:
            raise ValueError("a negative result is not allowed")

        return Money(euros, cents)


if __name__ == "__main__":
    print(Money(4, 50))
    print()

    e1 = Money(4, 25)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2 - e1

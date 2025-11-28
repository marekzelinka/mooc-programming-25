class Wallet:
    def __init__(self) -> None:
        self.__money: int = 0

    @property
    def money(self) -> int:
        return self.__money

    @money.setter
    def money(self, money: int) -> None:
        if money < 0:
            raise ValueError("Value must not be below zero")

        self.__money = money


if __name__ == "__main__":
    wallet = Wallet()
    print(wallet.money)

    wallet.money = 50
    print(wallet.money)

    wallet.money = -30
    print(wallet.money)

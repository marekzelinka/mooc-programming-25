class SavingsAccount:
    general_rate = 0.03

    def __init__(
        self, account_number: str, balance: float, interest_rate: float
    ) -> None:
        self.__acount_number: str = account_number
        self.__balance: float = balance
        self.__interest_rate: float = interest_rate

    def add_interest(self) -> None:
        self.__balance += self.__balance * self.total_interest

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def total_interest(self) -> float:
        """
        The total interest rate equals the general rate + the interest rate of the account
        """

        return SavingsAccount.general_rate + self.__interest_rate


if __name__ == "__main__":
    account1 = SavingsAccount("12345", 100, 0.03)
    account2 = SavingsAccount("54321", 200, 0.06)

    print(
        "General interest rate:", SavingsAccount.general_rate
    )  # General interest rate: 0.03
    print(account1.total_interest)  # 0.06
    print(account2.total_interest)  # 0.09

    # The general rate of interest is now 10 percent
    SavingsAccount.general_rate = 0.10

    print(
        "General interest rate:", SavingsAccount.general_rate
    )  # General interest rate: 0.1
    print(account1.total_interest)  # 0.13
    print(account2.total_interest)  # 0.16

class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float) -> None:
        self.__owner: str = owner
        self.__account_number: str = account_number
        self.__balance: float = balance

    def deposit(self, amount: float) -> None:
        if self.__check_amount(amount):
            raise ValueError("Amount must not be below zero")

        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount: float) -> None:
        if self.__check_amount(amount):
            raise ValueError("Amount must not be below zero")

        self.__balance -= amount
        self.__service_charge()

    @property
    def balance(self) -> float:
        return self.__balance

    def __service_charge(self) -> None:
        service_charge = self.__balance * 0.01
        self.__balance -= service_charge

    def __check_amount(self, amount: float) -> bool:
        return amount < 0


if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)  # 891.0
    account.deposit(100)
    print(account.balance)  # 981.09

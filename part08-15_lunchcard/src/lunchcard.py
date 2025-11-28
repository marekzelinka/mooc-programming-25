from typing import Literal


class LunchCard:
    def __init__(self, balance: int) -> None:
        self.balance = balance

    def __str__(self) -> str:
        return f"The balance is {self.balance:.1f} euros"

    def deposit_money(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")

        self.balance += amount

    def eat(self, meal: Literal["lunch", "special"]) -> None:
        prices = {"lunch": 2.6, "special": 4.6}
        new_balance = self.balance - prices[meal]

        if new_balance < 0:
            return

        self.balance = new_balance

    def eat_lunch(self) -> None:
        self.eat("lunch")

    def eat_special(self) -> None:
        self.eat("special")


peters_card = LunchCard(20)
graces_card = LunchCard(30)

peters_card.eat_special()
graces_card.eat_lunch()
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

peters_card.deposit_money(20)
graces_card.eat_special()
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

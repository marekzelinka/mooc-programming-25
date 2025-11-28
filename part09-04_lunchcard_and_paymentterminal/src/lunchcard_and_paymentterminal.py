# WRITE YOUR SOLUTION HERE:


class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float) -> bool:
        new_balance = self.balance - amount

        if new_balance < 0:
            return False

        self.balance = new_balance

        return True


class PaymentTerminal:
    def __init__(self) -> None:
        self.funds: float = 1000
        self.lunches: int = 0
        self.specials: int = 0

    def eat_lunch(self, payment: float) -> float:
        cost = 2.5
        change = payment - cost

        if payment < cost:
            return payment

        self.funds += cost
        self.lunches += 1

        return change

    def eat_special(self, payment: float) -> float:
        cost = 4.3
        change = payment - cost

        if payment < cost:
            return payment

        self.funds += cost
        self.specials += 1

        return change

    def eat_lunch_lunchcard(self, card: LunchCard) -> bool:
        cost = 2.5

        new_card_balance = card.balance - cost

        if new_card_balance < 0:
            return False

        card.balance = new_card_balance
        self.lunches += 1

        return True

    def eat_special_lunchcard(self, card: LunchCard):
        # A special lunch costs 4.30 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        cost = 4.3

        new_card_balance = card.balance - cost

        if new_card_balance < 0:
            return False

        card.balance = new_card_balance
        self.specials += 1

        return True

    def deposit_money_on_card(self, card: LunchCard, amount: float) -> None:
        card.balance += amount
        self.funds += amount


if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)

class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name: str = name
        self.price: float = price


class BonusCard:
    BONUS_PERCENTAGE = 0.05

    def __init__(self) -> None:
        self.products_bought: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products_bought.append(product)

    def calculate_bonus(self) -> float:
        return sum(
            [product.price * self.BONUS_PERCENTAGE for product in self.products_bought]
        )


class PlatinumCard(BonusCard):
    PLATINUM_BONUS_PERCENTAGE = 1.05

    def __init__(self) -> None:
        super().__init__()

    def calculate_bonus(self) -> float:
        bonus = super().calculate_bonus()

        return bonus * self.PLATINUM_BONUS_PERCENTAGE


if __name__ == "__main__":
    card = BonusCard()
    card.add_product(Product("Bananas", 6.50))
    card.add_product(Product("Satsumas", 7.95))
    bonus = card.calculate_bonus()

    card2 = PlatinumCard()
    card2.add_product(Product("Bananas", 6.50))
    card2.add_product(Product("Satsumas", 7.95))
    bonus2 = card2.calculate_bonus()

    print(bonus)
    print(bonus2)

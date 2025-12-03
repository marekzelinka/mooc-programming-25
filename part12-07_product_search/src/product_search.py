# Write your solution here
from collections.abc import Callable


def search(products: list, criterion: Callable):
    return list(filter(criterion, products))


if __name__ == "__main__":
    products = [
        ("banana", 5.95, 12),
        ("apple", 3.95, 3),
        ("orange", 4.50, 2),
        ("watermelon", 4.95, 22),
        ("kale", 0.99, 1),
    ]

    def price_under_4_euros(product):
        return product[1] < 4

    for product in search(products, price_under_4_euros):
        print(product)

    print()
    print()

    for product in search(products, lambda t: t[2] > 10):
        print(product)

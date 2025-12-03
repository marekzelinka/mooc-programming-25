def sort_by_price(items: list[tuple[str, float]]) -> list[tuple[str, float]]:
    def order_by_price(item: tuple) -> float:
        """Order by price, which is the second item within the tuple."""

        return item[1]

    return sorted(items, key=order_by_price)


if __name__ == "__main__":
    products = [
        ("banana", 5.95),
        ("apple", 3.95),
        ("orange", 4.50),
        ("watermelon", 4.95),
    ]

    for product in sort_by_price(products):
        print(product)

# TEE RATKAISUSI TÄHÄN:
class ShoppingList:
    def __init__(self) -> None:
        self.products: list[tuple[str, int]] = []

    def number_of_items(self) -> int:
        return len(self.products)

    def add(self, product: str, number: int) -> None:
        self.products.append((product, number))

    def product(self, n: int) -> str | None:
        try:
            return self.products[n - 1][0]
        except IndexError:
            return None

    def number(self, n: int) -> int | None:
        try:
            return self.products[n - 1][1]
        except IndexError:
            return None

    def __iter__(self) -> "ShoppingList":
        self.iter_counter = 0

        return self

    def __next__(self) -> tuple[str, int]:
        if self.iter_counter >= len(self.products):
            raise StopIteration

        product = self.products[self.iter_counter]
        self.iter_counter += 1

        return product


if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add("bananas", 10)
    shopping_list.add("apples", 5)
    shopping_list.add("pineapple", 1)

    for product in shopping_list:
        print(f"{product[0]}: {product[1]} units")

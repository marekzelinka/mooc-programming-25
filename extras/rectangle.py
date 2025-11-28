class Rectangle:
    def __init__(
        self, left_upper: tuple[int, int], right_lower: tuple[int, int]
    ) -> None:
        self.left_upper: tuple[int, int] = left_upper
        self.right_lower: tuple[int, int] = right_lower

        self.width: int = right_lower[0] - left_upper[0]
        self.height: int = right_lower[1] - left_upper[1]

    def area(self) -> int:
        return self.width * self.height

    def perimeter(self) -> int:
        return self.width * 2 + self.height * 2

    def move(self, x_change: int, y_change: int) -> None:
        corner = self.left_upper
        self.left_upper = (corner[0] + x_change, corner[1] + y_change)

        corner = self.right_lower
        self.right_lower = (corner[0] + x_change, corner[1] + y_change)

    def __str__(self) -> str:
        return f"rectangle {self.left_upper} ... {self.right_lower}"


if __name__ == "__main__":
    # rectangle = Rectangle((1, 1), (4, 3))
    # print(rectangle)

    # big_rectangle = Rectangle((1, 10), (10, 1))
    # print(big_rectangle)

    bigger_rectangle = Rectangle((10, 120), (100, 10))
    print(bigger_rectangle)
    # print(rectangle.left_upper)
    # print(rectangle.right_lower)
    print(bigger_rectangle.width)
    print(bigger_rectangle.height)
    # print(rectangle.perimeter())
    # print(rectangle.area())

    # rectangle.move(3, 3)
    # print(rectangle.left_upper)
    # print(rectangle.right_lower)

# Write your solution here!
class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height

    def area(self) -> int:
        return self.width * self.height

    def __str__(self) -> str:
        return f"rectangle {self.width}x{self.height}"


class Square(Rectangle):
    def __init__(self, size: int) -> None:
        super().__init__(size, size)

    def area(self):
        return self.width**2

    def __str__(self) -> str:
        return super().__str__().replace("rectangle", "square")


if __name__ == "__main__":
    rectangle = Rectangle(2, 3)
    print(rectangle)
    print("area:", rectangle.area())
    print()

    square = Square(4)
    print(square)
    print("area:", square.area())

# Write your solution here:
class Computer:
    def __init__(self, model: str, speed: int) -> None:
        self.__model: str = model
        self.__speed: int = speed

    @property
    def model(self) -> str:
        return self.__model

    @property
    def speed(self) -> float:
        return self.__speed


class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight: int) -> None:
        super().__init__(model, speed)
        self.__weight: int = weight

    @property
    def weight(self) -> int:
        return self.__weight

    def __str__(self) -> str:
        return f"{self.model}, {self.speed} MHz, {self.weight} kg"


if __name__ == "__main__":
    laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
    print(laptop)

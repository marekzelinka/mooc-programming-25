# Do not make changes to the class!
class Car:
    def __init__(self, make: str, top_speed: int) -> None:
        self.make: str = make
        self.top_speed: int = top_speed

    def __str__(self) -> str:
        return f"Car (make: {self.make}, top speed: {self.top_speed})"


def fastest_car(cars: list[Car]) -> str:
    return max(cars, key=lambda car: car.top_speed).make

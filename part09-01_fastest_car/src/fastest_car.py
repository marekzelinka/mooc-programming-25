# Do not make changes to the class!
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"


def fastest_car(cars: list[Car]) -> str:
    fastest = cars[0]

    for car in cars:
        if car.top_speed > fastest.top_speed:
            fastest = car

    return fastest.make

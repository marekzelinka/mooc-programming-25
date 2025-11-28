class Car:
    def __init__(self) -> None:
        self.__petrol = 0
        self.__odometer = 0

    def fill_up(self) -> None:
        self.__petrol += 60

    def drive(self, km: int) -> None:
        if km < 0:
            return

        new_petrol = self.__petrol - km

        if new_petrol < 0:
            return

        self.__petrol -= km
        self.__odometer += km

    def __str__(self) -> str:
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"


if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)

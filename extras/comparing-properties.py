class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int) -> None:
        self.__rooms: int = rooms
        self.__square_metres: int = square_metres
        self.__price_per_sqm: int = price_per_sqm

    @property
    def rooms(self) -> int:
        return self.rooms

    @property
    def square_metres(self) -> int:
        return self.square_metres

    @property
    def price_per_sqm(self) -> int:
        return self.price_per_sqm

    def __gt__(self, value: object) -> bool:
        if not isinstance(value, RealProperty):
            return False

        return self.__square_metres > value.__square_metres

    def __sub__(self, value: object) -> int:
        if not isinstance(value, RealProperty):
            return False

        price = self.__square_metres * self.__price_per_sqm
        compared_to_price = value.__square_metres * value.__price_per_sqm

        return abs(price - compared_to_price)

    @classmethod
    def more_expensive(cls, a: "RealProperty", b: "RealProperty") -> bool:
        price = a.__square_metres * a.__price_per_sqm
        compared_to_price = b.__square_metres * b.__price_per_sqm

        return price > compared_to_price


if __name__ == "__main__":
    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio > downtown_two_bedroom)
    print(suburbs_three_bedroom > downtown_two_bedroom)

    print(central_studio - downtown_two_bedroom)
    print(suburbs_three_bedroom - downtown_two_bedroom)

    print(RealProperty.more_expensive(central_studio, downtown_two_bedroom))
    print(RealProperty.more_expensive(suburbs_three_bedroom, downtown_two_bedroom))

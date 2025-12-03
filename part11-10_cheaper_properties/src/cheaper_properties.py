class RealProperty:
    def __init__(
        self, rooms: int, square_meters: int, price_per_sqm: int, description: str
    ):
        self.rooms: int = rooms
        self.square_meters: int = square_meters
        self.price_per_sqm: int = price_per_sqm
        self.description: str = description

    def bigger(self, compared_to: "RealProperty") -> bool:
        return self.square_meters > compared_to.square_meters

    def price_diff(self, compared_to: "RealProperty") -> int:
        difference = abs(
            (self.price_per_sqm * self.square_meters)
            - (compared_to.price_per_sqm * compared_to.square_meters)
        )

        return difference

    def more_expensive(self, compared_to: "RealProperty") -> bool:
        difference = (self.price_per_sqm * self.square_meters) - (
            compared_to.price_per_sqm * compared_to.square_meters
        )

        return difference > 0

    def __repr__(self) -> str:
        return (
            f"RealProperty(rooms = {self.rooms}, square_meters = {self.square_meters}, "
            + f"price_per_sqm = {self.price_per_sqm}, description = {self.description})"
        )


# WRITE YOUR SOLUTION HERE:
def cheaper_properties(lp: list[RealProperty], r: RealProperty):
    return [(p, p.price_diff(r)) for p in lp if p != r and not p.more_expensive(r)]


if __name__ == "__main__":
    a1 = RealProperty(1, 16, 5500, "Central studio")
    a2 = RealProperty(2, 38, 4200, "Two bedrooms downtown")
    a3 = RealProperty(3, 78, 2500, "Three bedrooms in the suburbs")
    a4 = RealProperty(6, 215, 500, "Farm in the middle of nowhere")
    a5 = RealProperty(4, 105, 1700, "Loft in a small town")
    a6 = RealProperty(25, 1200, 2500, "Countryside mansion")

    properties = [a1, a2, a3, a4, a5, a6]

    print(f"cheaper options when compared to {a3.description}:")

    for property, price_difference in cheaper_properties(properties, a3):
        print(f"{property.description:35} price difference {price_difference} euros")

import math

from point import Point


class Line:
    """
    Represents a line segment in two-dimensional space.
    """

    def __init__(self, beginning: Point, end: Point) -> None:
        self.beginning: Point = beginning
        self.end: Point = end

    def length(self) -> float:
        """Returns the length of the line segment calculated using the Pythagoream theorem."""

        sum_of_squares = (self.end.x - self.beginning.x) ** 2 + (
            self.end.y - self.beginning.y
        ) ** 2

        return math.sqrt(sum_of_squares)

    def centre_point(self) -> Point:
        """Returns the Point in the middle of the line segment."""

        centre_x = (self.beginning.x + self.end.x) / 2
        centre_y = (self.beginning.y + self.end.y) / 2

        return Point(centre_x, centre_y)

    def __str__(self) -> str:
        return f"{self.beginning} ... {self.end}"


if __name__ == "__main__":
    point = Point(1, 3)
    print(point)

    origo = Point.origo()
    print(origo)

    point2 = Point.mirrored(point, True, True)
    print(point2)

    line = Line(point, point2)
    print(line.length())
    print(line.centre_point())
    print(line)

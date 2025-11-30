class Point:
    """
    The class represents a point in two-dimensional space.
    """

    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    @classmethod
    def origo(cls) -> "Point":
        """Returns a new Point at origo (0, 0)"""

        return cls(0, 0)

    @classmethod
    def mirrored(cls, point: "Point", mirror_x: bool, mirror_y: bool) -> "Point":
        """
        Creates a new Point based on an existing Points.
        The original Point can be mirrored on either or both of the x and y axes.

        For example, the Point(1, 3) mirrored on the x-axis is (1, -3).
        """

        x = point.x
        y = point.y

        if mirror_x:
            y = -y

        if mirror_y:
            x = -x

        return cls(x, y)

    def __str__(self) -> str:
        return f"{self.x}, {self.y}"

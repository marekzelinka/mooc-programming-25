class Clock:
    MAX_HOURS = 23
    MAX_SECONDS_MINUTES = 59
    INITIAL = 0

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours: int = hours % (self.MAX_HOURS + 1)
        self.minutes: int = minutes % (self.MAX_SECONDS_MINUTES + 1)
        self.seconds: int = seconds % (self.MAX_SECONDS_MINUTES + 1)

    def tick(self) -> None:
        """
        Advances the clock by one second, handling rollovers sequentially.
        """

        self.seconds += 1

        if self.seconds > self.MAX_SECONDS_MINUTES:
            self.seconds = self.INITIAL
            self.minutes += 1

        if self.minutes > self.MAX_SECONDS_MINUTES:
            self.minutes = self.INITIAL
            self.hours += 1

        if self.hours > self.MAX_HOURS:
            # The clock has rolled over a full 24 hours
            self.hours = self.INITIAL

    def set(self, hours: int, minutes: int) -> None:
        self.hours = hours % (self.MAX_HOURS + 1)
        self.minutes = minutes % (self.MAX_SECONDS_MINUTES + 1)
        self.seconds = self.INITIAL

    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)

class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours: int = hours
        self.minutes: int = minutes
        self.seconds: int = seconds

    def tick(self) -> None:
        max_hours_value = 23
        max_seconds_minutes_value = 59
        initial = 0

        if (
            self.seconds == max_seconds_minutes_value
            and self.minutes == max_seconds_minutes_value
            and self.hours == max_hours_value
        ):
            self.hours = initial
            self.minutes = initial
            self.seconds = initial
        elif (
            self.seconds == max_seconds_minutes_value
            and self.minutes == max_seconds_minutes_value
        ):
            self.hours += 1
            self.minutes = initial
            self.seconds = initial
        elif self.seconds == max_seconds_minutes_value:
            self.minutes += 1
            self.seconds = 0
        else:
            self.seconds += 1

    def set(self, hours: int, minutes: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

    def __str__(self) -> str:
        return f"{str(self.hours).rjust(2, '0')}:{str(self.minutes).rjust(2, '0')}:{str(self.seconds).rjust(2, '0')}"


if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()

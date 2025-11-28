class Stopwatch:
    def __init__(self):
        self.seconds: int = 0
        self.minutes: int = 0

    def tick(self) -> None:
        max_value = 59
        initial = 0

        if self.minutes == max_value and self.seconds == max_value:
            self.seconds = initial
            self.minutes = initial
        elif self.seconds == max_value:
            self.seconds = initial
            self.minutes += 1
        else:
            self.seconds += 1

    def __str__(self) -> str:
        return f"{str(self.minutes).rjust(2, '0')}:{str(self.seconds).rjust(2, '0')}"


if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()

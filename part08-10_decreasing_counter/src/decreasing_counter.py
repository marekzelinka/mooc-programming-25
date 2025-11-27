# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int) -> None:
        self.initial_value = initial_value
        self.value = initial_value

    def print_value(self) -> None:
        print("value:", self.value)

    def decrease(self) -> None:
        if self.value == 0:
            return

        self.value -= 1

    # Write the rest of the methods here!
    def set_to_zero(self) -> None:
        self.value = 0

    def reset_original_value(self) -> None:
        self.value = self.initial_value


if __name__ == "__main__":
    counter = DecreasingCounter(55)
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()  # value: 51
    counter.reset_original_value()
    counter.print_value()  # value: 55

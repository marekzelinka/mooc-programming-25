class NumberStats:
    def __init__(self) -> None:
        self.numbers: list[int] = []

    def add_number(self, number: int) -> None:
        self.numbers.append(number)

    def count_numbers(self) -> int:
        return len(self.numbers)

    def get_sum(self) -> int:
        return sum(self.numbers)

    def average(self) -> float:
        if not self.count_numbers():
            return 0

        return self.get_sum() / self.count_numbers()


numbers = NumberStats()
even_numbers = NumberStats()
odd_numbers = NumberStats()

print("Please type in integer numbers:")

while True:
    number = int(input())

    if number == -1:
        break

    numbers.add_number(number)

    if number % 2 == 0:
        even_numbers.add_number(number)
    else:
        odd_numbers.add_number(number)


print(f"Sum of numbers: {numbers.get_sum()}")
print(f"Mean of numbers: {numbers.average()}")
print(f"Sum of even numbers: {even_numbers.get_sum()}")
print(f"Sum of odd numbers: {odd_numbers.get_sum()}")

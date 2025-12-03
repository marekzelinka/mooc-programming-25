# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, round: int, drawn_numbers: list[int]) -> None:
        self.round: int = round
        self.__drawn_numbers: list[int] = drawn_numbers[:7]

    def number_of_hits(self, numbers: list[int]) -> int:
        return len([number for number in numbers if self.__hit(number)])

    def hits_in_place(self, numbers: list[int]) -> list[int]:
        return [number if self.__hit(number) else -1 for number in numbers[:7]]

    def __hit(self, number: int) -> bool:
        return number in self.__drawn_numbers


if __name__ == "__main__":
    week5 = LotteryNumbers(5, [1, 2, 3, 4, 5, 6, 7])
    my_numbers = [1, 4, 7, 11, 13, 19, 24]

    print(week5.number_of_hits(my_numbers))

    week8 = LotteryNumbers(8, [1, 2, 3, 10, 20, 30, 33])
    my_numbers = [1, 4, 7, 10, 11, 20, 30]

    print(week8.hits_in_place(my_numbers))

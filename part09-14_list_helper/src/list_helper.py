class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list[int]) -> int:
        return max(set(my_list), key=my_list.count)

    @classmethod
    def doubles(cls, my_list: list[int]) -> int:
        return len([number for number in set(my_list) if my_list.count(number) > 1])


if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]  # [1, 3, 5]
    print(ListHelper.greatest_frequency(numbers))  # 5
    print(ListHelper.doubles(numbers))  # 3

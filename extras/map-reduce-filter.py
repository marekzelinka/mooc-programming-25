from functools import reduce

"""map function"""

str_list = ["123", "-10", "24", "15", "1", "0", "-110"]

integers = map(int, str_list)
# same as: integers = map(lambda x: int(x), str_list)

if __name__ == "__main__":
    print(integers)

    for n in integers:
        print(n)


def capitalize(string: str):
    first = string[0]
    first = first.upper()

    return first + string[1:]


test_list = ["first", "second", "third", "fourth"]

capitalized = map(capitalize, test_list)
# same as: map(str.capitalize, test_list)
# using for loops on a iterator only works once, after the iterator is depleted

capitalized_list = list(capitalized)

if __name__ == "__main__":
    print(capitalized_list)

    for word in capitalized_list:
        print(word)

    print("print the same again:")

    for word in capitalized_list:
        print(word)

"""filter function"""


integers = [1, 2, 3, 5, 6, 4, 9, 10, 14, 15]

even_numbers = filter(lambda number: number % 2 == 0, integers)
all_even_numbers = all(map(lambda n: n % 2 == 0, integers))

if __name__ == "__main__":
    print(f"Are all numbers even: {all_even_numbers}")

    for number in even_numbers:
        print(number)


class Fish:
    """Models a fish of a certain species and weight."""

    def __init__(self, species: str, weight: int) -> None:
        self.species = species
        self.weight = weight

    def __str__(self):
        return f"{self.species} ({self.weight} g.)"


if __name__ == "__main__":
    f1 = Fish("Pike", 1870)
    f2 = Fish("Perch", 763)
    f3 = Fish("Pike", 3410)
    f4 = Fish("Cod", 2449)
    f5 = Fish("Roach", 210)

    fishes = [f1, f2, f3, f4, f5]

    over_a_kilo = list(filter(lambda fish: fish.weight >= 1000, fishes))

    for fish in over_a_kilo:
        print(fish)

    # the same but with a list comprehension:
    # over_a_kilo = [fish for fish in fishes if fish.weight >= 1000]
    #
    # use this if you need to pass the resulting list elsewhere in the program

"""reduce function"""

my_list_of_numbers = [2, 2, 4, 3, 5, 2]

sum_of_numbers = reduce(lambda acc, curr: acc + curr, my_list_of_numbers, 0)
product_of_list = reduce(lambda acc, curr: acc * curr, my_list_of_numbers, 1)


if __name__ == "__main__":
    print(f"Sum of numbers: {sum_of_numbers}")
    print(f"Product of numbers: {product_of_list}")


class BankAccount:
    def __init__(self, account_number: str, name: str, balance: float) -> None:
        self.__account_number = account_number
        self.name = name
        self.__balance = balance

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError()

        self.__balance += amount

    @property
    def balance(self):
        return self.__balance


a1 = BankAccount("123456", "Randy Riches", 5000)
a2 = BankAccount("12321", "Paul Pauper", 1)
a3 = BankAccount("223344", "Mary Millionaire ", 1_000_000)

accounts = [a1, a2, a3]
balances_total = reduce(lambda acc, curr: acc + curr.balance, accounts, 0)

print(f"The total of the bank's balances is {balances_total}")

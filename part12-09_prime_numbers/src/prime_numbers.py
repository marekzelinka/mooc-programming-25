# Write your solution here
def is_prime(number: int):
    return all(number % i for i in range(2, number)) if number > 1 else False


def prime_numbers():
    number = 1

    while True:
        if is_prime(number):
            yield number

        number += 1


if __name__ == "__main__":
    numbers = prime_numbers()

    for i in range(62):
        print(next(numbers))

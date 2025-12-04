import string


def counter(max_value: int):
    number = 0
    while number <= max_value:
        yield number
        number += 1


if __name__ == "__main__":
    numbers = counter(2)

    # We can also traverse through all the items with a for loop
    for number in numbers:
        print(number)

    # This will now always raise an exception, because we have gone through all the values
    try:
        print("first value:")
        # we start the counter at zero so this works
        print(next(numbers))
        print("seconds value:")
        print(next(numbers))
        print("third value:")
        print(next(numbers))
        print("next value:")
        # next value is greater that start value, so this raises a StopIteration exception
        print(next(numbers))
    except StopIteration:
        print("ran out of numbers")

r = range(1, 64)
squares = (x**2 for x in r)

if __name__ == "__main__":
    print(squares)

    for i in range(5):
        print(next(squares))

substrings = (
    string.ascii_lowercase[i : i + 3] for i in range(len(string.ascii_lowercase))
)

if __name__ == "__main__":
    for i in range(10):
        print(next(substrings))

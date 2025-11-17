def spruce(height: int) -> None:
    print("a spruce!")

    i = 1

    while i <= height:
        spaces = height - i
        stars = 2 * i - 1
        print(f"{' ' * spaces}{'*' * stars}")

        i += 1

    print(" " * (height - 1) + "*")


if __name__ == "__main__":
    spruce(5)

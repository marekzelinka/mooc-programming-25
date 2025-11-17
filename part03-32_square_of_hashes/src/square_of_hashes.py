def hash_square(size: int) -> None:
    count = 0

    while count < size:
        print("#" * size)

        count += 1


if __name__ == "__main__":
    hash_square(5)

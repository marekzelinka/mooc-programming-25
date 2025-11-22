def times_ten(start_index: int, end_index: int) -> dict[int, int]:
    result = {}

    for i in range(start_index, end_index + 1):
        result[i] = i * 10

    return result


def main() -> None:
    d = times_ten(3, 6)
    print(d)  # {3: 30, 4: 40, 5: 50, 6: 60}


if __name__ == "__main__":
    main()

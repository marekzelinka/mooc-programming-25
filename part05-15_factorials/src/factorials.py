def factorials(n: int) -> dict[int, int]:
    result = {}

    for i in range(1, n + 1):
        if i == 1:
            result[i] = 1
        else:
            result[i] = result[i - 1] * i

    return result


def main() -> None:
    k = factorials(5)
    print(k[1])  # 1
    print(k[3])  # 6
    print(k[5])  # 120


if __name__ == "__main__":
    main()

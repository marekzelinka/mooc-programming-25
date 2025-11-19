def count_matching_elements(matrix: list[list[int]], element: int) -> int:
    matches: int = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == element:
                matches += 1

    return matches


def main() -> None:
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]

    print(count_matching_elements(m, 1))  # 3


if __name__ == "__main__":
    main()

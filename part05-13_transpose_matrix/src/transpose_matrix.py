def transpose(matrix: list[list[int]]) -> None:
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp


def main() -> None:
    matrix: list[list[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    transpose(matrix)

    print(matrix)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


if __name__ == "__main__":
    main()

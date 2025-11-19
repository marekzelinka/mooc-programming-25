def row_correct(sudoku_grid: list[list[int]], row_no: int) -> bool:
    row = sudoku_grid[row_no]

    for square in range(1, 10):
        square_count = row.count(square)

        if square_count > 1:
            return False

    return True


def main() -> None:
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))


if __name__ == "__main__":
    main()

def sudoku_column(grid: list[list[int]], col_no: int) -> list[int]:
    col_squares: list[int] = []

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if col == col_no:
                square = grid[row][col]
                col_squares.append(square)

    return col_squares


def column_correct(sudoku_grid: list[list[int]], col_no: int) -> bool:
    col = sudoku_column(sudoku_grid, col_no)

    for square in range(1, 10):
        square_count = col.count(square)

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

    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))


if __name__ == "__main__":
    main()

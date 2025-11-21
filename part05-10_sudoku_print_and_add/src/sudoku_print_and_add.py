def fix_empty_squares(grid: list[list[int | str]]) -> None:
    for row_no in range(len(grid)):
        for col_no in range(len(grid[row_no])):
            if grid[row_no][col_no] == 0:
                grid[row_no][col_no] = "_"


def print_sudoku(grid: list[list[int | str]]) -> None:
    fix_empty_squares(grid)

    for row_no in range(len(grid)):
        for col_no in range(len(grid[row_no])):
            print(grid[row_no][col_no], end=" ")

            col_block_end = (col_no + 1) % 3 == 0

            if col_block_end:
                print(end=" ")

        row_block_end = (row_no + 1) % 3 == 0

        if row_block_end:
            print()

        print()


def add_number(grid: list[list[int | str]], row_no: int, col_no: int, square: int):
    if square < 1 or square > 9:
        raise ValueError("Square must be between 1 and 9.")

    grid[row_no][col_no] = square


def main() -> None:
    sudoku: list[list[int | str]] = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)


if __name__ == "__main__":
    main()

from copy import deepcopy

from .types import Grid


def fix_empty_squares(grid: Grid) -> None:
    for row_no in range(len(grid)):
        for col_no in range(len(grid[row_no])):
            if grid[row_no][col_no] == 0:
                grid[row_no][col_no] = "_"


def print_sudoku(grid: Grid) -> None:
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


def copy_and_add(grid: Grid, row_no: int, col_no: int, square: int) -> Grid:
    updated = deepcopy(grid)

    updated[row_no][col_no] = square

    return updated


if __name__ == "__main__":
    sudoku: Grid = [
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

    fix_empty_squares(sudoku)

    grid_copy = copy_and_add(sudoku, 1, 1, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)

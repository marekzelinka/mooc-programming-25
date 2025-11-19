def row_correct(board: list[list[int]], row_no: int) -> bool:
    row = board[row_no]

    for square in range(1, 10):
        square_count = row.count(square)

        if square_count > 1:
            return False

    return True


def sudoku_column(board: list[list[int]], col_no: int) -> list[int]:
    col_squares: list[int] = []

    for row in range(len(board)):
        for col in range(len(board[row])):
            if col == col_no:
                square = board[row][col]

                col_squares.append(square)

    return col_squares


def column_correct(board: list[list[int]], col_no: int) -> bool:
    col = sudoku_column(board, col_no)

    for square in range(1, 10):
        square_count = col.count(square)

        if square_count > 1:
            return False

    return True


def board_block(board: list[list[int]], row_no: int, col_no: int) -> list[int]:
    block: list[int] = []

    BLOCK_SIZE = 3

    for i in range(row_no, row_no + BLOCK_SIZE):
        for j in range(col_no, col_no + BLOCK_SIZE):
            square = board[i][j]

            block.append(square)

    return block


def block_size_correct(row_no: int, col_no: int) -> bool:
    BLOCK_SIZE = 3

    return row_no % BLOCK_SIZE == 0 and col_no % BLOCK_SIZE == 0


def block_correct(board: list[list[int]], row_no: int, col_no: int) -> bool:
    block = board_block(board, row_no, col_no)

    for square in range(1, 10):
        square_count = block.count(square)

        if square_count > 1:
            return False

    return True


def sudoku_grid_correct(sudoku: list[list[int]]) -> bool:
    for row_no in range(len(sudoku)):
        if not row_correct(sudoku, row_no):
            return False

        for col_no in range(len(sudoku[row_no])):
            if not column_correct(sudoku, col_no):
                return False

            if block_size_correct(row_no, col_no) and not block_correct(
                sudoku, row_no, col_no
            ):
                return False

    return True


def main() -> None:
    sudoku1 = [
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

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1],
    ]

    print(sudoku_grid_correct(sudoku2))


if __name__ == "__main__":
    main()

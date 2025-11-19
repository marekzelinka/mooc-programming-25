def board_block(board: list[list[int]], row_no: int, col_no: int) -> list[int]:
    block: list[int] = []

    block_size = 3

    for i in range(row_no, row_no + block_size):
        for j in range(col_no, col_no + block_size):
            square = board[i][j]

            block.append(square)

    return block


def block_correct(board: list[list[int]], row_no: int, col_no: int) -> bool:
    block = board_block(board, row_no, col_no)

    for square in range(1, 10):
        square_count = block.count(square)

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

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))


if __name__ == "__main__":
    main()

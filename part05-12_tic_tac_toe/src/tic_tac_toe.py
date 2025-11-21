from .types import Board, Piece


def play_turn(board: Board, x: int, y: int, piece: Piece) -> bool:
    # Check if y (row) coordinate is valid
    if y < 0 or y >= len(board):
        return False

    # Check if x (column) coordinate is valid
    if x < 0 or x >= len(board[y]):
        return False

    square = board[y][x]

    if square == "":
        board[y][x] = piece

        return True

    return False


def main() -> None:
    game_board: Board = [["", "", ""], ["", "", ""], ["", "", ""]]

    print(play_turn(game_board, 2, 0, "X"))  # True
    print(game_board)  # [['', '', 'X'], ['', '', ''], ['', '', '']]


if __name__ == "__main__":
    main()

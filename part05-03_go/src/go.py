def count_squares(board: list[list[int]], player: int) -> int:
    count = 0

    for row in board:
        for col in row:
            if col == player:
                count += 1

    return count


def who_won(game_board: list) -> int:
    player_a_squares = count_squares(game_board, 1)
    player_b_squares = count_squares(game_board, 2)

    if player_a_squares == player_b_squares:
        return 0
    elif player_a_squares > player_b_squares:
        return 1
    else:
        return 2


def main() -> None:
    game_board = [[1, 2, 1], [0, 0, 1], [2, 1, 0]]
    winner = who_won(game_board)

    print(winner)


if __name__ == "__main__":
    main()

def chessboard(length: int) -> None:
    row = 0

    while row < length:
        col = 0

        while col < length:
            if (row + col) % 2 == 0:
                print(1, end="")
            else:
                print(0, end="")

            col += 1

        print()

        row += 1


if __name__ == "__main__":
    chessboard(3)

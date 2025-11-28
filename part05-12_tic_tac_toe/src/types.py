from typing import Literal

type Piece = Literal["", "X", "O"]

type Board = list[list[Piece]]

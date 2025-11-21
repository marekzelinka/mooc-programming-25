from typing import Literal

type Piece = Literal[""] | Literal["X"] | Literal["O"]

type Board = list[list[Piece]]

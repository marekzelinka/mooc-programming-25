from random import shuffle


class DeckOfCards:
    def __init__(self) -> None:
        self.__reset_deck()

    def __reset_deck(self) -> None:
        # Create a new deck with all 52 cards
        self.__deck = [
            (suit, number)
            for suit in ["spades", "hearts", "clubs", "diamonds"]
            for number in range(1, 14)
        ]

        # Shuffle the deck
        shuffle(self.__deck)

    def deal(self, count: int) -> list[tuple[str, int]]:
        hand = [self.__deck.pop() for i in range(count)]

        return hand


if __name__ == "__main__":
    deck = DeckOfCards()
    hand1 = deck.deal(5)
    print(hand1)
    hand2 = deck.deal(5)
    print(hand2)

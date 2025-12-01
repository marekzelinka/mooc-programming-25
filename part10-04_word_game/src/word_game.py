# Write your solution here
import random


class WordGame:
    def __init__(self, rounds: int) -> None:
        self.wins1: int = 0
        self.wins2: int = 0
        self.rounds: int = rounds

    def round_winner(self, player1_word: str, player2_word: str) -> int:
        # determine a random winner
        return random.randint(1, 2)

    def play(self) -> None:
        print("Word game:")

        for i in range(1, self.rounds + 1):
            print(f"round {i}")

            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1

                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1

                print("player 2 won")
            else:
                pass  # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int) -> None:
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str) -> int:
        """whoever types in the longest word on each round wins."""

        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return 0


class MostVowels(WordGame):
    def __init__(self, rounds: int) -> None:
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str) -> int:
        """Whoever has squeezed more vowels into their word wins the round."""

        if self.__count_wowels(player1_word) > self.__count_wowels(player2_word):
            return 1
        elif self.__count_wowels(player2_word) > self.__count_wowels(player1_word):
            return 2
        else:
            return 0

    def __count_wowels(self, word: str):
        return sum(word.count(vowel) for vowel in ["a", "e", "i", "o", "u"])


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int) -> None:
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str) -> int:
        """
        If the input from either player is invalid, they lose the round.
        If both players type in something else than rock, paper or scissors, the result is a tie.
        The rules of the game are as follows:
        - rock beats scissors (the rock can break the scissors but the scissors can't cut the rock)
        - paper beats rock (the paper can cover the rock)
        - scissors beats paper (the scissors can cut the paper)
        """

        if not self.__valid_hand(player1_word) and not self.__valid_hand(player2_word):
            return 0  # it is a tie
        elif self.__valid_hand(player1_word) and not self.__valid_hand(player2_word):
            return 2  # input from player 1 is invalid, player 2 wins
        elif self.__valid_hand(player2_word) and not self.__valid_hand(player1_word):
            return 1  # input from player 2 is invalid, player 1 wins

        if (
            (player1_word == "rock" and player2_word == "scissors")
            or (player1_word == "paper" and player2_word == "rock")
            or (player1_word == "scissors" and player2_word == "paper")
        ):
            return 1
        elif (
            (player2_word == "rock" and player1_word == "scissors")
            or (player2_word == "paper" and player1_word == "rock")
            or (player2_word == "scissors" and player1_word == "paper")
        ):
            return 2
        else:
            return 0

    def __valid_hand(self, hand: str) -> bool:
        return hand in ["rock", "paper", "scissors"]


if __name__ == "__main__":
    p = RockPaperScissors(4)
    p.play()

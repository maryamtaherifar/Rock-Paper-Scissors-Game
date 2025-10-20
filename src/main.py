"""Rock Paper Scissors game
Author: Taheri far
Date created: 10/20/2025
"""

import random
from termcolor import cprint
from utils.end_of_game import end_of_game
from utils.game_again import game_again


class Game:
    """Main class for Rock Paper Scissors game."""
    def __init__(self, limit: int):
        self.limit = limit

    def computer_choice(self) -> str:
        return random.choice(['Rock', 'Paper', 'Scissors'])

    def user_choice(self) -> str:
        user_choice = input('1: Rock\n2: Paper\n3: Scissors\n')
        if user_choice not in {'1', '2', '3'}:
            print('Invalid input! Try again.')
            return self.user_choice()
        if user_choice == '1':
            return 'Rock'
        elif user_choice == '2':
            return 'Paper'
        elif user_choice == '3':
            return 'Scissors'

    def compare(self, computer: str, user: str) -> str:
        """Decide the winner of the round.

        :param computer: The choice of the computer
        :param user: The choice of the user
        :return: The winner of the round: 'You' or 'Computer'
        """
        choice_combinations = [('Rock', 'Scissors'), ('Scissors', 'Paper'), ('Paper', 'Rock')]
        if computer == user:
            winner = None
        elif (user, computer) in choice_combinations:
            winner = 'You'
        else:
            winner = 'Computer'
        return winner

    def run(self):
        """Play the game.
        - Get computer choice.
        - Get user choice.
        - Decide the winner.
        - Print the result.
        """
        scores = {
            'Computer': 0,
            'You': 0
        }

        while True:
            if end_of_game(scores, self.limit):
                break

            computer = self.computer_choice()
            print("The computer has chosen, it's your turn:")
            user = self.user_choice()
            winner = self.compare(computer, user)
            if winner is not None:
                scores[winner] += 1
            cprint(f"The coputer choice: {computer}\nYour choice: {user}", color= 'white', on_color='on_yellow')
            cprint('Scores:', color= 'white', on_color='on_yellow')
            for p, s in scores.items():
                cprint(f"{p}: {s}", color= 'white', on_color='on_yellow')

        if game_again(scores):
            return self.run()


if __name__ == '__main__':
    RPS = Game(3)
    RPS.run()
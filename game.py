"""
A model for the game acheivments and probably methods for scoring.
"""


STARTING_MOVES = [
    'One of a Kind 1s',
    'One of a Kind 2s',
    'One of a Kind 3s',
    'One of a Kind 4s',
    'One of a Kind 5s',
    'One of a Kind 6s'
]


def ask_for_category(final_dice):
    next_move = input("How do you want to get points? ")
    print(STARTING_MOVES)


class Game:
    def one_of_a_kind(final_dice):
        pass

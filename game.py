"""
A model for the game acheivments and probably methods for scoring.
"""


STARTING_MOVES = [
    'ones',
    'twos'
]

running_points = 0
# class Game:
#
#     def __init__(self):
#         self.running_points = 0
#         self.categories_used = []
#
#     def add_to_running_points(running_points, points_to_add):
#         running_points = running_points + points_to_add
#         return(running_points)


def ask_for_category(final_dice):
    next_move = input("How do you want to get points? ")
    if next_move == 'ones':
        return record_ones(final_dice, running_points)
    if next_move == 'twos':
        return record_twos(final_dice, running_points)
    else:
        pass


def record_ones(final_dice, running_points):
    all_dice = []
    for key, value in final_dice['kept'].items():
        all_dice.append(value)
    for key, value in final_dice['reroll'].items():
        all_dice.append(value)
    number_of_ones = 0
    for die in all_dice:
        if die == 1:
            number_of_ones += 1
    total_ones_points = number_of_ones * 1
    running_points += total_ones_points
    return(running_points)


def record_twos(final_dice, running_points):
    all_dice = []
    for key, value in final_dice['kept'].items():
        all_dice.append(value)
    for key, value in final_dice['reroll'].items():
        all_dice.append(value)
    number_of_twos = 0
    for die in all_dice:
        if die == 2:
            number_of_twos += 1
    total_twos_points = number_of_twos * 2
    running_points += total_twos_points
    return(running_points)

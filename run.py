from roll import *
from game import *


dice = first_roll()
final_dice = second_roll(dice)
get_next_move_points = ask_for_category(final_dice)
print("Your total points are now: ", running_points)
dice = first_roll()
final_dice = second_roll(dice)
get_next_move_points = ask_for_category(final_dice)
print("Your total points are now: ", running_points)

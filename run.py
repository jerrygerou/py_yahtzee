from roll import *
from game import *


game = Game()
dice = first_roll()
final_dice = second_roll(dice)
kept_dice = final_dice.get("kept")
kept_dice_values = []
for key, value in kept_dice:
    kept_dice_values.add(key)
print(kept_dice_values)
get_next_move_points = Game().ask_for_category(kept_dice_values)
print("Your total points are now: ", Game().get_running_points())
# dice = first_roll()
# final_dice_again = second_roll(dice)
# get_next_move_points = Game().ask_for_category(final_dice_again)
# print("Your total points are now: ", Game().get_running_points())

from roll import *
from game import *


dice = first_roll()
final_dice = second_roll(dice)
get_next_move = ask_for_category(final_dice)

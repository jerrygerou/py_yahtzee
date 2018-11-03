"""
Methods for actually rolling the dice... maybe should live with Dice?
"""

from dice import Dice


def turn():
    # Each turn should have two rolls
    pass


def first_roll():
    # First roll should just initiate 5 dice.
    dice = {}
    for i in range(5):
        die = Dice()
        dice[i] = die
    for key, value in dice.items():
        print("Die:", key, "Value:", value.value)

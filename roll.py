"""
Methods for actually rolling the dice... maybe should live with Dice?
"""
import random

from dice import Dice


def turn():
    # Each turn should have two rolls
    pass


def second_roll(dice):
    print(dice)
    if dice['reroll']:
        for key, value in dice['reroll'].items():
            dice['reroll'][key] = random.randint(1,6)
            print(key, value)
    for key, value in dice['kept'].items():
        print(" _____ ")
        print("|     |")
        print("|  %d  |" % value)
        print("|_____|")
    for key, value in dice['reroll'].items():
        print(" _____ ")
        print("|     |")
        print("|  %d  |" % value)
        print("|_____|")


def first_roll():
    # First roll should just initiate 5 dice.
    dice = {}
    for i in range(1, 6):
        die = Dice()
        dice[i] = die
    for key, value in dice.items():
        print(" _____ ")
        print("|     |")
        print("|  %d  |" % value.value)
        print("|_____|")
    responses = {}
    responses['kept'] = {}
    responses['reroll'] = {}
    for key, value in dice.items():
        keep = input("Would you like to keep Die %d ? (Y or N) " % key)
        if keep == "Y" or keep == "y":
            print("we'll keep the value")
            responses['kept'][key] = value.value
        elif keep == "N" or keep == "n":
            print("You can roll this again.")
            responses['reroll'][key] = value.value
    print(responses)
    return responses


        # print("Die:", key, "Value:", value.value)
    # question = input("Which dice would you like to hold?")
    # print(question)

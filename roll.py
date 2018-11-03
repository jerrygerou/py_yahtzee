"""
Methods for actually rolling the dice... maybe should live with Dice?
"""

from dice import Dice


def turn():
    # Each turn should have two rolls
    pass


def second_roll(dice):
    for d in dice:
        print(d)


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
    for key, value in dice.items():
        keep = input("Would you like to keep Die %d ? (Y or N) " % key)
        if keep == "Y":
            print("we'll keep the value")
        elif keep == "N":
            print("You can roll this again.")
            responses[key] = value.value
    print(responses)
    return responses


        # print("Die:", key, "Value:", value.value)
    # question = input("Which dice would you like to hold?")
    # print(question)

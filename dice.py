import random


class Dice:
    """
    A model class for a six-sided die.
    """
    def __init__(self):
        self.value = random.randint(1, 6)

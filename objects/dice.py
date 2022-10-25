import random

dice_tags = {'d6': ['Steel', 'Wood', 'Leather'],
             'd8': ['Elemental', 'Wood', 'Leather'],
             'd10': ['Elemental', 'Arcane', 'Leather'],
             'd12': ['Elemental', 'Arcane', 'Wild']
             }


def d6():
    value = random.randint(1, 6)
    return value


def d8():
    value = random.randint(1, 8)
    return value


def d10():
    value = random.randint(1, 10)
    return value


def d12():
    value = random.randint(1, 12)
    return value


class Die:
    def __init__(self, die_type):
        self.value = eval(die_type+"()")
        self.tags = dice_tags[die_type]


class DiceSet:
    def __init__(self):
        self.d6 = Die('d6')
        self.d8 = Die('d8')
        self.d10 = Die('d10')
        self.d12 = Die('d12')

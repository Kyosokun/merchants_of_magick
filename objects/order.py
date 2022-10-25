from objects.deck import Deck


class Order:
    name = None
    affixes = []
    value = 0

    def __init__(self, affix_list, value):
        self.affixes = []
        for affix in affix_list:
            if self.name:
                self.name = self.name + " " + affix
            else:
                self.name = affix
        self.affixes.extend(affix_list)
        self.value = value


class OrderDeck(Deck):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for order in orders:
            self.add(Order(order[0], order[1]))
            self.shuffle()


orders = [[['everlasting', 'backpack'], 2],
          [['backpack', 'of the Dwarves'], 2],
          [['everlasting', 'backpack', 'of the Dragons'], 5],
          [['fiery', 'scroll'], 2],
          [['divine', 'scroll'], 3],
          [['scroll', 'of the Elves'], 2],
          [['shocking', 'ring'], 3],
          [['ring', 'of the Dwarves'], 3],
          [['divine', 'pendant'], 3],
          [['grimoire', 'of the Elves'], 3],
          [['grimoire', 'of the Dragons'], 4]
          ]

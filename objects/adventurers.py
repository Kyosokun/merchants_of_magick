from deck import Deck


class Adventurer:
    def __init__(self, name, value, enchantment, items):
        self.name = name
        self.value = value
        self.enchantment = enchantment
        self.items = items


class AdventurerDeck(Deck):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for adventurer in adventurers:
            name = adventurer[0]
            value = adventurer[1]
            enchantment = adventurer[2]
            items = adventurer[3]
            self.add(Adventurer(name, value, enchantment, items))

    def random_card(self, remove=True):
        return super().random_card(remove)


adventurers = [['The Warrior', 6, 'of the Dwarves', ['grimoire', 'crossbow', 'bracers']],
               ['The Wizard', 4, 'shocking', ['scroll', 'staff', 'greaves']],
               ['The Berserker', 6, 'of the Orcs', ['ring', 'spear', 'helmet']],
               ['The Priest', 6, 'divine', ['pendant', 'warhammer', 'shield']]
               ]

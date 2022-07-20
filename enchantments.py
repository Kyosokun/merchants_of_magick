from affixes import Affix, affix_collection


class Enchantment(Affix):
    def __init__(self, name, value, requirements):
        super().__init__(name, value, requirements)
        self.affix_type = 'magical'
        self.affix_class = 'enchantment'


enchantments = [['fiery', 1, [['elemental', 6], ['wild', 11]]],
                ['shocking', 2, [['elemental', 2], ['arcane', 7]]],
                ['everlasting', 2, [['arcane', 1], ['wild', 9]]],
                ['divine', 3, [['elemental', 9], ['arcane', 2], ['wild', 7]]],
                ['of the Elves', 1, [['arcane', 8], ['wild', 10]]],
                ['of the Dwarves', 2, [['elemental', 8], ['arcane', 4]]],
                ['of the Orcs', 3, [['elemental', 7], ['wild', 4]]],
                ['of the Dragons', 4, [['elemental', 5], ['arcane', 6], ['wild', 2]]]
                ]

enchantment_collection = affix_collection(Enchantment, enchantments)

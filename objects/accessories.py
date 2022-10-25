from affixes import Affix, affix_collection


class Accessory(Affix):
    def __init__(self, name, value, requirements):
        super().__init__(name, value, requirements)
        self.affix_type = 'physical'
        self.affix_class = 'accessory'


accessories = [['backpack', 1, [['leather', 3]]],
               ['scroll', 1, [['wood', 3]]],
               ['ring', 2, [['steel', 2], ['leather', 6]]],
               ['pendant', 2, [['wood', 7], ['leather', 1]]],
               ['grimoire', 3, [['steel', 5], ['wood', 4], ['leather', 4]]]
               ]

accessory_collection = affix_collection(Accessory, accessories)

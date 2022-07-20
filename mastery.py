from deck import Deck


class Mastery:
    def __init__(self, name, material, marks):
        self.master_name = f"Master {name}"
        self.apprentice_name = f"Apprentice {name}"
        self.material = material
        self.marks = marks
        value = 8


class MasteryDeck(Deck):
    def __init__(self, masteries):
        for mastery in masteries:
            self.add(Mastery(mastery[0], mastery[1], mastery[2]))


material_masteries = [['Blacksmith', 'steel', 4],
                      ['Carpenter', 'wood', 5],
                      ['Leatherworker', 'leather', 6]
                      ]


energy_masteries = [['Elementalist', 'elemental', 6],
                    ['Arcanist', 'arcane', 5],
                    ['Druid', 'wild', 4]
                    ]

material_deck = MasteryDeck(material_masteries)
energy_deck = MasteryDeck(energy_masteries)

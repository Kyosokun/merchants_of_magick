from accessories import accessory_collection
from enchantments import enchantment_collection


class Player:
    player_number = 0
    shop_name = 'Player'
    potions = 0
    extra_dice_available = [4, 3, 3, 0, 0, 0]
    material_mastery_marks = 0
    energy_mastery_marks = 0
    affixes = {}
    completed_affixes = []
    sponsored_adventurer = None
    adventurer_orders_completed = 0
    completed_orders = []
    crafting_points = 0
    material_mastery_points = 0
    research_points = 0
    energy_mastery_points = 0
    order_points = 0
    charm_bonus = 0
    adventurer_points = 0
    total_points = 0

    def __init__(self, player_number, adventurer, name=None):
        self.player_number = player_number
        self.shop_name = name or f'Shop {player_number}'
        self.sponsored_adventurer = adventurer
        self.affixes.update(accessory_collection)
        self.affixes.update(enchantment_collection)

    def complete_order(self, order):
        self.completed_orders.append(order)
        self.order_points += order.value

    def check_mastery(self, mastery):
        result = False
        if mastery.material in ['steel', 'wood', 'leather']:
            result = self.check_material_mastery(mastery)
        elif mastery.material in ['enchantment', 'arcane', 'wild']:
            result = self.check_material_mastery(mastery)
        return result

    def check_material_mastery(self, mastery):
        if (self.material_mastery_marks >= mastery.marks) and self.material_mastery_points == 0:
            self.material_mastery_points = mastery.value
            return True
        return False

    def check_energy_mastery(self, mastery):
        if (self.energy_mastery_marks >= mastery.marks) and self.energy_mastery_points == 0:
            self.energy_mastery_points = mastery.value
            return True
        return False

    def check_order_completion(self, order):
        for affix in order.affixes:
            if affix in self.completed_affixes:
                continue
            else:
                return False
        self.complete_order(order)
        return True

    def check_adventurer_orders(self):
        # jaaaaanky, try to improve
        completions = 0
        if self.sponsored_adventurer.enchantment in self.completed_affixes:
            for item in self.sponsored_adventurer.items:
                if item in self.completed_affixes:
                    # self.sponsored_adventurer.items.pop(item)
                    completions += 1
        new_completions = completions - self.adventurer_orders_completed
        while new_completions < 0:
            if (new_completions + self.adventurer_orders_completed) == 1:
                self.potions += 3
            elif (new_completions + self.adventurer_orders_completed) == 2:
                # player gets to mark 1 circle
                pass
            elif (new_completions + self.adventurer_orders_completed) == 3:
                # player gets to mak 1 circle
                self.adventurer_points = self.sponsored_adventurer.value
            new_completions -= 1
        self.adventurer_orders_completed = completions

    def mark_requirement_complete(self, die, affix_name, material):
        if self.affixes[affix_name].affix_type == 'physical':
            if die.value >= self.affixes[affix_name].requirements[material]['target']:
                self.affixes[affix_name].requirements[material]['completed'] = True
        if self.affixes[affix_name].affix_type == 'magical':
            if die.value <= self.affixes[affix_name].requirements[material]['target']:
                self.affixes[affix_name].requirements[material]['completed'] = True
        completed = True
        for req in self.affixes[affix_name].requirements.values():
            if not req['completed']:
                completed = False
        self.affixes[affix_name].completed = completed
        if completed:
            self.completed_affixes.append(affix_name)




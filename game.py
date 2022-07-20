from player import Player
from order import OrderDeck
from adventurers import AdventurerDeck
from mastery import material_deck, energy_deck
from dice import DiceSet
from deck import Deck


class Game(object):
    def __init__(self, player_count):
        """
        Setups up the game objects based on the number of players
        :param (int) player_count: the number of players playing
        :return: None
        """
        self.turn_number = 1
        self.dice_set = DiceSet()
        self.order_deck = OrderDeck()
        self.material_mastery = material_deck.random_card()
        self.energy_mastery = energy_deck.random_card()
        self.players = []
        self.in_play_orders = Deck()
        self.order_counts = 0
        adventurer_deck = AdventurerDeck()

        for x in range(player_count):
            self.players.append(Player(x, adventurer_deck.random_card()))

        if player_count in [1, 2]:
            self.order_counts = 4
        elif player_count in [3, 4, 5, 6]:
            self.order_counts = 3
        elif player_count in [7, 8]:
            self.order_counts = 2
        else:
            raise Exception("Player Count invalid")
        self.in_play_orders.add(self.order_deck.deal(num=player_count * self.order_counts))
        print()

    def advance_turn(self):
        self.turn_number += 1
        self.dice_set = DiceSet()
        for order in self.in_play_orders:
            if order is None:
                order = self.order_deck.deal()[0]
        self.in_play_orders.cards.rotate()

    def mastery_phase(self):
        for mastery in [self.material_mastery, self.energy_mastery]:
            claimed = False
            for player in self.players:
                result = player.check_mastery(mastery)
                if result:
                    claimed = True
            if claimed is True:
                if mastery.value == 8:
                    mastery.value = 4
                if mastery.value == 4:
                    mastery.value = 0

    def orders_phase(self):
        for player in self.players:
            bump = player.player_number * self.order_counts
            for x in range(self.order_counts):
                order = self.in_play_orders[x + bump]
                result = player.check_order_completion(order)
                if result:
                    self.in_play_orders[x + bump] = None
                if player.adventurer_orders_completed < 3:
                    player.check_adventurer_orders()
            print()

    def playing_phase(self):
        """
        janky rough automated implementation
        :return:
        """
        for player in self.players:
            # select die, drop it on attribute
            affix_name = 'ring'
            die = self.dice_set.d6
            material = 'steel'
            player.mark_requirement_complete(die, affix_name, material)

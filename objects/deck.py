from operator import attrgetter
from pydealer import Stack


class Deck(Stack):
    _cards = []

    def __str__(self):
        pass

    def sort(self, ranks=None):
        self.cards = sorted(self.cards, key=attrgetter('value'))




import random

from .AbstractPile import AbstractPile
from .Card import Card


class Deck(AbstractPile):
    def __init__(self):
        super().__init__()
        self._init()

    def _init(self):
        colors = ["Red", "Green", "Blue", "White", "Yellow"]
        for color in colors:
            for i in range(2, 11):  # Number cards
                self._cards.append(Card(color, i))
            for _ in range(3):  # Wager cards
                self._cards.append(Card(color, 0))

    def shuffle(self):
        random.shuffle(self._cards)

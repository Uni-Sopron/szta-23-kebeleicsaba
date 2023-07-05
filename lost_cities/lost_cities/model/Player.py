from .AbstractPile import AbstractPile
from .Card import Card
from .DiscardPile import DiscardPile
from .Expedition import Expedition
from .Hand import Hand


class Player:
    def __init__(self, name: str):
        self._name = name
        self._hand = Hand()
        self._expeditions = {
            color: Expedition(color)
            for color in ["Red", "Green", "Blue", "White", "Yellow"]
        }

    def play_card(self, card: Card, expedition: Expedition):
        pass

    def discard_card(self, card: Card, discard_pile: DiscardPile):
        pass

    def draw_card(self, pile: AbstractPile):
        pass

    def select_card(self):
        pass

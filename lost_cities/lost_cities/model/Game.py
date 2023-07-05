from typing import List

from .Deck import Deck
from .DiscardPile import DiscardPile
from .Expedition import Expedition
from .Player import Player


class Game:
    def __init__(self, player_names: List[str]):
        self._deck = Deck()
        self._discard_piles = {
            color: DiscardPile(color)
            for color in ["Red", "Green", "Blue", "White", "Yellow"]
        }
        self._expeditions = {
            color: Expedition(color)
            for color in ["Red", "Green", "Blue", "White", "Yellow"]
        }
        self._players = [Player(name) for name in player_names]
        self._current_player = self._players[0]

    def start(self):
        self._deck.shuffle()
        for player in self._players:
            for _ in range(8):
                player.draw_card(self._deck)

    def turn(self, player: Player):
        pass

    def calculate_scores(self):
        pass

    def end(self):
        pass

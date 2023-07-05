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

    def turn(self, player: Player, action: dict):
        # {"type": "play" or "discard", "card": card,
        # "location": color, "draw_from": "deck" or color}
        card_to_play = action["card"]

        if action["type"] == "play":
            player.play_card(card_to_play, action["location"])
        elif action["type"] == "discard":
            player.discard_card(card_to_play, self._discard_piles[action["location"]])

        if action["draw_from"] == "deck":
            player.draw_card(self._deck)
        else:
            player.draw_card(self._discard_piles[action["draw_from"]])

    def calculate_scores(self):
        for player in self._players:
            score = 0
            for color, expedition in player._expeditions.items():
                value = sum(card.get_value() for card in expedition._cards)
                if value > 0:
                    value -= 20
                    multipliers = expedition._cards.count(0)
                    value *= multipliers + 1
                    if len(expedition._cards) >= 8:
                        value += 20
                score += value
            player._score = score

    def end(self) -> bool:
        return self._deck.is_empty()

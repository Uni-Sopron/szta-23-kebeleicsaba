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
        self._players = [Player(name) for name in player_names]
        self._current_player = self._players[0]
        self._current_turn = 1

    def start(self):
        self._deck.shuffle()
        for player in self._players:
            for _ in range(8):
                player.draw_card(self._deck)

    def turn(self, player: Player, action: dict):
        # {"type": "play" or "discard", "card": card, "location": color, "draw_from": "deck" or color}
        if action["type"] == "play":
            player.play_card(action["card"], action["location"])
        elif action["type"] == "discard":
            discard_pile = self._discard_piles[action["location"]]
            player.discard_card(action["card"], discard_pile)
        else:
            raise ValueError("Invalid action type. Must be 'play' or 'discard'.")

        if action["draw_from"] == "deck":
            if self._deck.get_top_card():
                player.draw_card(self._deck)
            else:
                self.end()
        else:
            discard_pile = self._discard_piles[action["draw_from"]]
            player.draw_card(discard_pile)

        # switch to the next player
        self._current_player = self._players[
            (self._players.index(self._current_player) + 1) % len(self._players)
        ]
        self._current_turn += 1

    def end(self) -> dict:
        for player in self._players:
            player.getPoints()
        return {player._name: player.getPoints() for player in self._players}

    def is_game_over(self) -> bool:
        return self._deck.is_empty()

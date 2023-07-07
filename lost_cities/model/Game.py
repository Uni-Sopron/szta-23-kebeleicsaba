from typing import List

from .Deck import Deck
from .DiscardPile import DiscardPile
from .Player import Player


class Game:
    """
    A játék irányításáért felelős osztály.
    """

    def __init__(self, player_names: List[str]):
        """
        Játék osztály létrehozása.

        Args:
            player_names (List[str]): A játékosok neveinek listája.
        """
        self._deck = Deck()
        self._discard_piles = {
            color: DiscardPile(color)
            for color in ["Red", "Green", "Blue", "White", "Yellow"]
        }
        self._players = [Player(name) for name in player_names]
        self._current_player = self._players[0]
        self._current_turn = 1

    def setup(self):
        """
        Beállítja a játék kezdő állapotát, azaz megkeveri a paklit és minden játékosnak oszt 8 lapot.
        """
        self._deck.shuffle()
        for player in self._players:
            for _ in range(8):
                player.draw_card(self._deck)

    def switch_player(self):
        """
        Váltja a soron következő játékost.
        """
        if self._current_player == self._players[0]:
            self._current_player = self._players[1]
        else:
            self._current_player = self._players[0]

    def get_game_points(self) -> dict:
        """
        Visszaadja a játékosok pontjait.

        Returns:
            dict: Egy dict, ahol kulcsok a játékosok nevei, az értékek pedig a játékosok pontjai.
        """
        for player in self._players:
            player.get_points()
        return {player._name: player.get_points() for player in self._players}

    def is_game_over(self) -> bool:
        """
        Megvizsgálja, hogy vége van-e már a játéknak.

        Returns:
            bool: Igaz, ha a játéknak vége (a pakli üres), egyébként hamis.
        """
        return self._deck.is_empty()

    def get_current_player(self):
        return self._current_player

    def get_discard_piles(self):
        return self._discard_piles

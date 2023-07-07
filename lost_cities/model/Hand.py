from typing import List

from .Card import Card


class Hand:
    def __init__(self) -> None:
        """
        Kéz osztály létrehozása. A kézben lévő lapokat tárolja.
        """
        self._cards: List[Card] = []

    def get_hand(self) -> list:
        """
        Visszaadja a kézben lévő lapokat.

        Returns:
            list: A kézben lévő lapok listája.
        """
        return self._cards

    def has_color(self, color: str) -> bool:
        """
        Megvizsgálja, hogy a kézben van-e adott színű lap.

        Args:
            color (str): A keresett lap színe.

        Returns:
            bool: Igaz, ha van a kézben adott színű lap, egyébként hamis.
        """
        return any(card.get_color() == color for card in self._cards)

    def remove_card(self, card: Card):
        """
        Eltávolít egy lapot a kézből.

        Args:
            card (Card): Az eltávolítandó lap.
        """
        self._cards.remove(card)

    def add_card(self, card: Card) -> None:
        """
        Hozzáad egy lapot a kézhez.

        Args:
            card (Card): A hozzáadandó lap.
        """
        self._cards.append(card)

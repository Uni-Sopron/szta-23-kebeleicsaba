from typing import Optional

from .AbstractPile import AbstractPile
from .Card import Card


class DiscardPile(AbstractPile):
    """
    Az eldobott lapokat tartalmazó pakli.
    """

    def __init__(self, color: str):
        """
        Inicializálja a dobó paklit kártyák nélkül és egy megadott színnel.

        Args:
            color (str): A pakli színe.
        """
        super().__init__()
        self._color = color

    def get_color(self):
        """
        Visszaadja a pakli színét.
        """
        return self._color

    def add_card(self, card: Card):
        """
        Hozzáad egy lapot a paklihoz.

        Args:
            card (Card): A hozzáadandó lap.
        """
        self._cards.append(card)

    def display_top_card(self) -> Optional[Card]:
        """
        Visszaadja a pakli tetején lévő lapot.

        Returns:
            Optional[Card]: A pakli tetején lévő lap, vagy `None`, ha a pakli üres.
        """
        return self._cards[-1] if self._cards else None

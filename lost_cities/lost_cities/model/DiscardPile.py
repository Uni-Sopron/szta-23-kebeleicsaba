from .AbstractPile import AbstractPile
from .Card import Card


class DiscardPile(AbstractPile):
    def __init__(self, color: str):
        super().__init__()
        self._color = color

    def get_color(self):
        return self._color

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def display_top_card(self) -> Card:
        return self._cards[-1]

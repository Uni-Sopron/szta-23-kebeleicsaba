from typing import List

from .Card import Card


class Hand:
    def __init__(self) -> None:
        self._cards: List[Card] = []

    def get_hand(self) -> list:
        return self._cards

    def has_color(self, color: str) -> bool:
        return any(card.get_color() == color for card in self._cards)

    def remove_card(self, card: Card):
        self._cards.remove(card)

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

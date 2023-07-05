from typing import List

from .Card import Card


class Expedition:
    def __init__(self, color: str) -> None:
        self._cards: List[Card] = []
        self._color = color

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def remove_card(self, card: Card) -> None:
        self._cards.remove(card)

    def contains_wager(self) -> bool:
        return any(card.get_value() == 0 for card in self._cards)

    def highest_value(self) -> int:
        if not self._cards:
            return 0
        return max(card.get_value() for card in self._cards)

    def get_color(self) -> str:
        return self._color

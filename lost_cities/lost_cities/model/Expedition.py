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
        return self._cards[-1].get_value()

    def get_color(self) -> str:
        return self._color

    def get_points(self) -> int:
        if not self._cards:
            return 0

        base_score = sum(
            card.get_value() for card in self._cards if card.get_value() != 0
        )
        base_score -= 20
        wager_multiplier = sum(1 for card in self._cards if card.get_value() == 0) + 1
        base_score *= wager_multiplier

        if len(self._cards) >= 8:
            base_score += 20

        return base_score

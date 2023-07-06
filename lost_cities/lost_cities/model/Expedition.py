from typing import List

from .Card import Card


class Expedition:
    """
    Az Expedíció osztály egy adott színhez tartozó lapok sora.
    """

    def __init__(self, color: str):
        """
        Inicializálja az expedíciót egy adott színnel.

        Args:
            color (str): Az expedíció színe.
        """
        self._cards: List[Card] = []
        self._color = color

    def add_card(self, card: Card):
        """
        Hozzáad egy lapot az expedícióhoz.

        Args:
            card (Card): A lap, melyet hozzáadunk az expedícióhoz.
        """
        self._cards.append(card)

    def remove_card(self, card: Card):
        """
        Eltávolít egy lapot az expedícióból.
        """
        self._cards.remove(card)

    def highest_value(self) -> int:
        """
        Visszaadja az expedícióban lévő utolsó lapot, ami legmagasabb értékű is egyben.

        Returns:
            int: a legnagyobb érték
        """
        if not self._cards:
            return 0
        return self._cards[-1].get_value()

    def get_color(self) -> str:
        """
        Visszaadja az expedíció színét.

        Returns:
            str: Az expedíció színe.
        """
        return self._color

    def get_points(self) -> int:
        """
        Kiszámítja és visszaadja az expedíció pontszámát.

        Returns:
            int: Az expedíció értéke pontszámba.
        """
        if not self._cards:
            return 0

        base_score = sum(
            card.get_value() for card in self._cards if card.get_value() != 0
        )
        base_score -= 20
        wager_multiplier = sum(1 for card in self._cards if card.get_value() == 0) + 1
        base_score *= wager_multiplier

        if len(self._cards) >= 8:
            base_score += (
                20 * wager_multiplier
            )  # A bónuszpontokat is meg kell szorozni a zálogkártyák számával

        return base_score

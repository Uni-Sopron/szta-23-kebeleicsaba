from typing import List, Union

from .Card import Card


class AbstractPile:
    def __init__(self) -> None:
        self._cards: List[Card] = []

    def is_empty(self) -> bool:
        return len(self._cards) == 0

    def get_top_card(self) -> Union[Card, None]:
        if self.is_empty():
            return None
        else:
            return self._cards.pop()

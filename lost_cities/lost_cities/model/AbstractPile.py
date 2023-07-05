from typing import List, Optional

from .Card import Card


class AbstractPile:
    """
    Az AbstractPile a kártya paklik absztrakt osztálya
    """

    def __init__(self) -> None:
        """
        Inicializálja a paklit egy üres listaként.
        """
        self._cards: List[Card] = []

    def is_empty(self) -> bool:
        """
        Megvizsgálja, hogy a pakli üres-e.

        Returns:
            bool: Igaz, ha a pakli üres. ellenkező esetben hamis.
        """
        return len(self._cards) == 0

    def get_top_card(self) -> Optional[Card]:
        """
        Lekéri a pakli tetején lévő kártyát. Ha a pakli üres, akkor None-t ad vissza.

        Returns:
            Optional[Card]: A pakli tetején lévő kártya, vagy None, ha a pakli üres.
        """
        if self.is_empty():
            return None
        else:
            return self._cards.pop()

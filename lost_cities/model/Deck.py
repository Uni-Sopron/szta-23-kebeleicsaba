import random

from .AbstractPile import AbstractPile
from .Card import Card


class Deck(AbstractPile):
    """
    A pakli osztály, amelyben kezdetben a játék összes lapja található.
    """

    def __init__(self):
        """
        Inicializálja a paklit, feltöltve azt a kezdeti lapokkal.
        """
        super().__init__()
        self._init()

    def _init(self):
        """
        Feltölti a paklit a játék kezdetén.
        """
        colors = ["Red", "Green", "Blue", "White", "Yellow"]
        for color in colors:
            for i in range(2, 11):
                self._cards.append(Card(color, i))
            for _ in range(3):
                self._cards.append(Card(color, 0))

    def shuffle(self):
        """
        Megkeveri a paklit.
        """
        random.shuffle(self._cards)

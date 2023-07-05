from .AbstractPile import AbstractPile


class DiscardPile(AbstractPile):
    def __init__(self, color: str):
        super().__init__()
        self._color = color

    def get_color(self):
        return self._color

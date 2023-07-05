class Card:
    def __init__(self, color: str, value: int) -> None:
        self._color = color
        self._value = value

    def get_color(self) -> str:
        return self._color

    def get_value(self) -> int:
        return self._value

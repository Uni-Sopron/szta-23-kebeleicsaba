class Card:
    """
    A Card osztály regy kártyát eprezentál, amelynek van színe és értéke.
    """

    def __init__(self, color: str, value: int):
        """
        Létrehoz egy új kártyát a megadott színnel és értékkel.

        Args:
            color (str): A kártya színe.
            value (int): A kártya értéke.
        """
        self._color = color
        self._value = value

    def get_color(self) -> str:
        """
        Lekéri a kártya színét.

        Returns:
            str: A kártya színe.
        """
        return self._color

    def get_value(self) -> int:
        """
        Lekéri a kártya értékét.

        Returns:
            int: A kártya értéke.
        """
        return self._value

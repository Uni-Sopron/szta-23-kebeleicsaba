from .AbstractPile import AbstractPile
from .Card import Card
from .DiscardPile import DiscardPile
from .Expedition import Expedition
from .Hand import Hand


class Player:
    """
    A játékos osztály.
    """

    def __init__(self, name: str) -> None:
        """
        Játékos osztály létrehozása.

        Args:
            name (str): A játékos neve.
        """
        self._name = name
        self._hand = Hand()
        self._expeditions = {
            color: Expedition(color)
            for color in ["Red", "Green", "Blue", "White", "Yellow"]
        }
        self._points = 0

    def play_card(self, card: Card, expedition: str) -> None:
        """
        Kijátsza a kártyát egy expedícióra.

        Args:
            card (Card): A kijátszanó kártya.
            expedition (str): Az expedíció színe, ahová a kártyát ki szeretnénk játszani.

        Raises:
            ValueError: Ha a játékosnak nincs ilyen kártyája, a kártya színe nem egyezik az expedíció színével,
                        vagy a kártya értéke kisebb mint az expedíció legnagyobb kártyájának értéke.
        """
        if card in self._hand.get_hand():
            if card.get_color() == expedition:
                if (
                    card.get_value() > self._expeditions[expedition].highest_value()
                    or card.get_value() == 0
                ):
                    self._expeditions[expedition].add_card(card)
                    self._hand.remove_card(card)
                else:
                    raise ValueError("Small value of the card")
            else:
                raise ValueError("The card color must be same as expedition color.")
        else:
            raise ValueError("The player does not have this card.")

    def discard_card(self, card: Card, discard_pile: DiscardPile) -> None:
        """
        Eldobja a kártyát egy dobó pakliba.

        Args:
            card (Card): Az eldobandó kártya.
            discard_pile (DiscardPile): Az dobó pakli, ahová a kártyát dobni szeretnénk.

        Raises:
            ValueError: Ha a játékosnak nincs ilyen kártyája, vagy a kártya színe nem egyezik az dobó pakli színével.
        """
        if card in self._hand.get_hand():
            if card.get_color() == discard_pile.get_color():
                discard_pile._cards.append(card)
                self._hand._cards.remove(card)
            else:
                raise ValueError("The card color must be same as discard pile color.")
        else:
            raise ValueError("The player does not have this card.")

    def draw_card(self, pile: AbstractPile):
        """
        Felhúz egy kártyát egy pakliból.

        Args:
            pile (AbstractPile): A pakli, ahonnan fel szeretnénk húzni a kártyát.

        Raises:
            ValueError: Ha a pakli üres.
        """
        if pile.is_empty():
            raise ValueError("The pile is empty.")
        else:
            self._hand.add_card(pile.get_top_card())

    def calc_points(self) -> None:
        """
        Kiszámolja a játékos pontjait az összes expedíciók a pontjai alapján és hozzáadja az eddigi pontszámhoz.
        """
        self._points += sum(
            expedition.get_points() for expedition in self._expeditions.values()
        )

    def get_points(self) -> int:
        """
        Visszaadja a játékos pontjait.

        Returns:
            int: A játékos pontjai.
        """
        return self._points

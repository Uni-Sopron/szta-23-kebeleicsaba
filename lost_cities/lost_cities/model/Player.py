from .AbstractPile import AbstractPile
from .Card import Card
from .DiscardPile import DiscardPile
from .Expedition import Expedition
from .Hand import Hand


class Player:
    def __init__(self, name: str) -> None:
        self._name = name
        self._hand = Hand()
        self._expeditions = {
            color: Expedition(color)
            for color in ["Red", "Green", "Blue", "White", "Yellow"]
        }

    def play_card(self, card: Card, expedition: str) -> None:
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
        if card in self._hand.get_hand():
            if card.get_color() == discard_pile.get_color():
                discard_pile._cards.append(card)
                self._hand._cards.remove(card)
            else:
                raise ValueError("The card color must be same as discard pile color.")
        else:
            raise ValueError("The player does not have this card.")

    def draw_card(self, pile: AbstractPile) -> None:
        card = pile.get_top_card()
        if card:
            self._hand._cards.append(card)
        else:
            raise ValueError("The pile is empty.")

    def select_card(self, card: Card) -> Card:
        if card in self._hand.get_hand():
            self._hand.remove_card(card)
            return card
        else:
            raise ValueError("The player does not have this card.")

import pytest

from lost_cities.model import Card, Hand


def test_initial_hand_empty():
    hand = Hand()
    assert hand.get_hand() == []


def test_has_color_empty_hand():
    hand = Hand()
    assert not hand.has_color("Red")


def test_remove_card_empty_hand():
    hand = Hand()
    with pytest.raises(ValueError):
        hand.remove_card(Card("Red", 2))


def test_add_card_to_hand():
    hand = Hand()
    card = Card("Red", 2)
    hand.add_card(card)
    assert hand.get_hand() == [card]


def test_remove_card_from_hand():
    hand = Hand()
    card = Card("Red", 2)
    hand.add_card(card)
    hand.remove_card(card)
    assert hand.get_hand() == []


def test_has_color_with_card():
    hand = Hand()
    hand.add_card(Card("Red", 2))
    assert hand.has_color("Red")


def test_has_color_with_only_other_color():
    hand = Hand()
    hand.add_card(Card("Red", 2))
    hand.add_card(Card("Yellow", 4))
    assert not hand.has_color("Blue")

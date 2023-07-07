from unittest.mock import Mock

from lost_cities.model import Card, DiscardPile


class TestDiscardPile:
    def setup_method(self):
        self.discard_pile = DiscardPile("Red")
        self.mock_card_1 = Mock(spec=Card)
        self.mock_card_2 = Mock(spec=Card)

    def test_get_color(self):
        assert self.discard_pile.get_color() == "Red"

    def test_add_card(self):
        assert len(self.discard_pile._cards) == 0
        self.discard_pile.add_card(self.mock_card_1)
        assert len(self.discard_pile._cards) == 1
        assert self.discard_pile._cards[0] == self.mock_card_1

    def test_display_top_card_empty_pile(self):
        assert self.discard_pile.display_top_card() is None

    def test_display_top_card_non_empty_pile(self):
        self.discard_pile.add_card(self.mock_card_1)
        assert self.discard_pile.display_top_card() == self.mock_card_1
        self.discard_pile.add_card(self.mock_card_2)
        assert self.discard_pile.display_top_card() == self.mock_card_2

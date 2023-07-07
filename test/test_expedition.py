from unittest.mock import Mock, patch

from lost_cities.model import Card, Expedition


class TestExpedition:
    def setup_method(self):
        self.expedition = Expedition("Red")
        self.mock_card_1 = Mock()
        self.mock_card_1.get_value.return_value = 5
        self.mock_card_2 = Mock()
        self.mock_card_2.get_value.return_value = 7
        self.mock_card_3 = Mock()
        self.mock_card_3.get_value.return_value = 9

    def test_add_card(self):
        self.expedition.add_card(self.mock_card_1)
        assert len(self.expedition._cards) == 1
        assert self.expedition._cards[0] == self.mock_card_1

    def test_highest_value(self):
        self.expedition.add_card(self.mock_card_1)
        assert self.expedition.highest_value() == 5

        self.expedition.add_card(self.mock_card_2)
        assert self.expedition.highest_value() == 7

    def test_add_multiple_cards(self):
        self.expedition.add_card(self.mock_card_1)
        self.expedition.add_card(self.mock_card_2)
        self.expedition.add_card(self.mock_card_3)
        assert len(self.expedition._cards) == 3
        assert self.expedition._cards[0] == self.mock_card_1
        assert self.expedition._cards[1] == self.mock_card_2
        assert self.expedition._cards[2] == self.mock_card_3
        assert self.expedition.highest_value() == 9

    @patch("lost_cities.model.Card")
    def test_get_points_no_cards(self, MockCard):
        expedition = Expedition("Red")
        assert expedition.get_points() == 0

    @patch("lost_cities.model.Card")
    def test_get_points_with_regular_cards(self, MockCard):
        mock_card_1 = Mock()
        mock_card_1.get_value.return_value = 0
        mock_card_2 = Mock()
        mock_card_2.get_value.return_value = 5
        mock_card_3 = Mock()
        mock_card_3.get_value.return_value = 9

        expedition = Expedition("Red")
        expedition.add_card(mock_card_1)
        expedition.add_card(mock_card_2)
        expedition.add_card(mock_card_3)

        assert expedition.get_points() == -12

    def test_get_points_with_wager_card_only(self):
        expedition = Expedition("Red")
        card = Card("Red", 0)
        expedition.add_card(card)
        assert expedition.get_points() == -40

    def test_get_points_with_multiple_wager_cards(self):
        expedition = Expedition("Red")
        for _ in range(3):
            card = Card("Red", 0)
            expedition.add_card(card)
        assert expedition.get_points() == -80

    def test_get_points_with_wager_card_and_regular_cards(self):
        # 2 + 4 + 5 + 8 + 9 = 28
        # (28 - 20) * 3 = 24
        expedition = Expedition("Red")
        expedition.add_card(Card("Red", 0))
        expedition.add_card(Card("Red", 0))
        expedition.add_card(Card("Red", 2))
        expedition.add_card(Card("Red", 4))
        expedition.add_card(Card("Red", 5))
        expedition.add_card(Card("Red", 8))
        expedition.add_card(Card("Red", 9))
        assert expedition.get_points() == 24

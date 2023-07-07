from lost_cities.model import Card, Expedition


class TestExpedition:
    def setup_method(self):
        self.expedition = Expedition("Red")
        self.card_1 = Card("Red", 5)
        self.card_2 = Card("Red", 7)
        self.card_3 = Card("Red", 9)

    def test_add_card(self):
        self.expedition.add_card(self.card_1)
        assert len(self.expedition._cards) == 1
        assert self.expedition._cards[0] == self.card_1

    def test_highest_value(self):
        self.expedition.add_card(self.card_1)
        assert self.expedition.highest_value() == 5

        self.expedition.add_card(self.card_2)
        assert self.expedition.highest_value() == 7

    def test_add_multiple_cards(self):
        self.expedition.add_card(self.card_1)
        self.expedition.add_card(self.card_2)
        self.expedition.add_card(self.card_3)
        assert len(self.expedition._cards) == 3
        assert self.expedition._cards[0] == self.card_1
        assert self.expedition._cards[1] == self.card_2
        assert self.expedition._cards[2] == self.card_3
        assert self.expedition.highest_value() == 9

    def test_get_points_no_cards(self):
        expedition = Expedition("Red")
        assert expedition.get_points() == 0

    def test_get_points_with_regular_cards(self):
        card_1 = Card("Red", 0)
        card_2 = Card("Red", 5)
        card_3 = Card("Red", 9)

        expedition = Expedition("Red")
        expedition.add_card(card_1)
        expedition.add_card(card_2)
        expedition.add_card(card_3)

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

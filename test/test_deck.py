from lost_cities.model import Deck


class TestDeckInit:
    def setup_method(self):
        self.deck = Deck()

    def test_deck_card_count(self):
        assert len(self.deck._cards) == 60

    def test_deck_color_counts(self):
        color_counts = {"Red": 0, "Green": 0, "Blue": 0, "White": 0, "Yellow": 0}
        for card in self.deck._cards:
            color_counts[card.get_color()] += 1

        for color in color_counts:
            assert color_counts[color] == 12

    def test_deck_wager_count(self):
        wager_count = 0
        for card in self.deck._cards:
            if card.get_value() == 0:
                wager_count += 1
        assert wager_count == 15

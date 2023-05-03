from Cards import Cards

class Hand(Cards):
    def get_cards(self) -> list:
        pass

class Player:
    def __init__(self, name:str) -> None:
        self._name = name
        self._points = 0
        self.hand = Hand()

    def get_name(self) -> str:
        pass

    def get_points(self) -> int:
        pass

    def get_hand(self) -> list:
        pass

    def play_card_to_expeditions(self, card, expedition) -> None:
        pass

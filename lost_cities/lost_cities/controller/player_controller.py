from ..model.Card import Card
from ..model.Player import Player


class PlayerController:
    def __init__(self, player: Player):
        self.player = player

    def play_card(self, card, expedition):
        self.player.play_card(card, expedition)

    def discard_card(self, card, discard_pile):
        self.player.discard_card(card, discard_pile)

    def draw_card(self, pile):
        self.player.draw_card(pile)

    def select_card(self, card) -> Card:
        return self.player.select_card(card)

    def take_turn(self, action):
        if action["type"] == "play":
            self.play_card(action["card"], action["location"])
        elif action["type"] == "discard":
            self.discard_card(action["card"], action["location"])

    def draw(self, game_controller, location):
        game_controller.draw_card(self.player, location)

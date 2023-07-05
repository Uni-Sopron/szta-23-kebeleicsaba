from ..model.Game import Game
from .player_controller import PlayerController


class GameController:
    def __init__(self, player_names):
        self.game = Game(player_names)
        self.player_controllers = [
            PlayerController(player) for player in self.game._players
        ]

    def start_game(self):
        self.game.start()

    def execute_turn(self, player_controller, action) -> bool:
        self.game.turn(player_controller.player, action)
        return self.game.end()

    def draw_card(self, player_controller, location):
        if location == "deck":
            player_controller.draw_card(self.game._deck)
        else:
            player_controller.draw_card(self.game._discard_piles[location])

    def calculate_scores(self):
        self.game.calculate_scores()

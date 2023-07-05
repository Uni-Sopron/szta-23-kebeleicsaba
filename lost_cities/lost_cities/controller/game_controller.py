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
        game_over = False
        while not game_over:
            for player_controller in self.player_controllers:
                action = {}
                game_over = self.execute_turn(player_controller, action)
                if game_over:
                    break
        self.calculate_scores()

    def execute_turn(self, player_controller, action) -> bool:
        player_controller.take_turn(self, action)
        return self.game.end()

    def draw_card(self, player_controller, location):
        if location == "deck":
            player_controller.draw_card(self.game._deck)
        else:
            player_controller.draw_card(self.game.discard_pile)

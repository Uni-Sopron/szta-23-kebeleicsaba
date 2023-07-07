from ..model.Game import Game
from ..view.console_view import ConsoleView


class GameController:
    def __init__(self, player_names):
        self.view = ConsoleView()
        self.player_names = self.view.get_player_names()
        self.number_of_rounds = 3
        self.game = Game(player_names)

    def turn(self):
        pass

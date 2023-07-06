from ..model.Game import Game


class GameController:
    def __init__(self, player_names):
        self.game = Game(player_names)

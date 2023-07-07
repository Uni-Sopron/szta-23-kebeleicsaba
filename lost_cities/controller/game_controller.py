from ..model.Game import Game


class GameController:
    def __init__(self, view):
        self.view = view
        self.player_names = self.view.get_player_names()
        self.number_of_rounds = 3
        self.game = Game(self.player_names)

    def turn(self):
        self.game.setup()
        d = self.view.get_player_decision()
        print(d)
        print("Hello Universe")

    def main(self):
        for _ in range(self.number_of_rounds):
            self.turn()

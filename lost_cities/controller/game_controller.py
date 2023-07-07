from ..model.Game import Game


class GameController:
    def __init__(self, view):
        self.view = view
        self.player_names = self.view.get_player_names()
        self.number_of_rounds = 3
        self.game = Game(self.player_names)

    def player_decision(self):
        d = self.view.get_player_decision(self.game.get_current_player().get_hand())
        if d == "play":
            pass
        else:
            pass

    def turn(self):
        self.view.print_expeditions(self.game.get_current_player())
        self.view.print_board(self.game.get_discard_piles())
        self.player_decision()
        self.game.switch_player()

    def main(self):
        for _ in range(self.number_of_rounds):
            self.game.setup()
            self.turn()

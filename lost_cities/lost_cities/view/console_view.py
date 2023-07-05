from ..controller import GameController


class ConsoleView:
    def __init__(self):
        self.game_controller = None

    def start(self):
        print("Welcome to Lost Cities Game!")
        player_names = self.get_player_names()
        self.game_controller = GameController(player_names)
        self.game_controller.start_game()

        while not self.game_controller.game.is_game_end():
            for controller in self.game_controller.player_controllers:
                print(f"Current player: {controller.player.name}")
                self.player_turn(controller)
        self.show_scores()

    def get_player_names(self):
        player_names = []
        for i in range(2):
            name = input(f"Enter name for player {i+1}: ")
            player_names.append(name)
        return player_names

    def player_turn(self, player_controller):
        print(f"Your hand: {player_controller.player.hand}")
        action_type = input("Enter action type (play/discard): ")
        card = input("Enter card to perform action on: ")
        expedition = input("Enter expedition to perform action on: ")
        action = {"type": action_type, "card": card, "location": expedition}
        self.game_controller.execute_turn(player_controller, action)
        pile = input("Enter pile to draw from (deck or discard pile number): ")
        self.game_controller.draw_card(player_controller, pile)

    def show_scores(self):
        self.game_controller.calculate_scores()
        for player in self.game_controller.game._players:
            print(f"{player.name} score: {player.score}")

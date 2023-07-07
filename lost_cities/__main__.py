from .controller.game_controller import GameController
from .view.console_view import ConsoleView

if __name__ == "__main__":
    v = ConsoleView()
    c = GameController(v)
    # c.main()

from typing import List

from ..controller import GameController


class ConsoleView:
    """
    A ConsoleView osztály kezeli a konzolon történő játékmenetet.
    """

    def __init__(self):
        """
        Konzolos játék osztály inicializálása.
        """
        self.start()

    def start(self):
        """
        Elindítja a játékot. Bekéri a játékosok nevét és a körök számát.
        """
        print("Welcome to Lost Cities Game!")
        self.player_names = self.get_player_names()
        self.number_of_rounds = self.get_number_of_rounds()
        self.game_controller = GameController(self.player_names)

    def get_number_of_rounds(self) -> int:
        """
        Bekéri a játékosoktól a körök számát.

        Returns:
            int: A körök száma.
        """
        n = int(input("Enter the number of rounds: "))
        return n

    def get_player_names(self) -> List[str]:
        """
        Bekéri a játékosok nevét.

        Returns:
            List[str]: A játékosok neveinek listája.
        """
        player_names = []
        for i in range(2):
            name = input(f"Enter name for player {i+1}: ")
            player_names.append(name)
        return player_names

from typing import List


class ConsoleView:
    """
    A ConsoleView osztály kezeli a konzolon történő játékmenetet.
    """

    def __init__(self):
        """
        Üdvözlő szöveg.
        """
        print("Welcome to Lost Cities Game!")

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

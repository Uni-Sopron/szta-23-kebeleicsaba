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

    def get_player_decision(self) -> str:
        """
        Bekéri a felhasználótol, hogy el szeretné-e dobni a kártyát (discard), vagy le szeretné-e játszani (play).
        play: 1
        discard: 0

        Returns:
            str: A játékos döntése ("discard" vagy "play").
        """
        while True:
            decision = input(
                "Would you like to discard a card (0) or play a card (1)? Enter the number: "
            )
            if decision == "1":
                return "play"
            elif decision == "0":
                return "discard"
            else:
                print("Invalid input. Please enter either 0 (discard) or 1 (play).")

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

    def get_player_decision(self, hand) -> str:
        """
        Bekéri a felhasználótol, hogy el szeretné-e dobni a kártyát (discard), vagy le szeretné-e játszani (play).
        play: 1
        discard: 0

        Returns:
            str: A játékos döntése ("discard" vagy "play").
        """
        print("\nYour hand: " + str(hand))
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

    def get_card_from_hand(self, hand):
        """
        Kéri a játékostól, hogy válasszon egy kártyát a kezéből.

        Args:
            hand (list): A játékos kártyáinak listája.

        Returns:
            Card: A játékos által választott kártya.
        """
        print("\nYour hand: " + str(hand))
        while True:
            chosen_color = input(
                "Please enter the color of the card you want to select from your hand: "
            )
            chosen_value = int(
                input(
                    "Please enter the value of the card you want to select from your hand: "
                )
            )

            for card in hand:
                if (
                    card.get_color() == chosen_color
                    and card.get_value() == chosen_value
                ):
                    return card

            print("The card you selected is not in your hand. Please choose again.")

    def print_board(self, piles):
        print("\nDiscard piles:")
        for color in ["Red", "Green", "Blue", "White", "Yellow"]:
            if not piles[color].is_empty():
                print(color + ": top card" + piles[color].display_top_card())
            else:
                print(color + ": empty")

    def print_expeditions(self, player):
        print("\n" + player.get_name() + " expeditions:")
        for color in ["Red", "Green", "Blue", "White", "Yellow"]:
            print(color + ": " + str(player.get_expeditions()[color].get_expedition()))

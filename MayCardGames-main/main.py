# ~~~~~ IMPORTED OBJECTS ~~~~
from blackjackManager import BlackJackManager


# ~~~~~ MAIN FUNCTION DEFINITION ~~~~~
def main():
    appOn = True
    blackjack = BlackJackManager()
    while appOn:
        print("")
        print(" ~~~~~ CARD GAMES ~~~~~")
        print("")
        print("1. Blackjack")
        print("2. Quit")
        print("")
        choice = input(" --> ").lower()
        
        if choice in ["1", "1.", "blackjack"]:
            blackjack.playGame()
        elif choice in ["2", "2.", "quit"]:
            appOn = False
        else:
            print("Invalid option - choose again!")


# ~~~~~ MAIN FUNCTION CALL ~~~~~
if __name__ == "__main__":
    main()

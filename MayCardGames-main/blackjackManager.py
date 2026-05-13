from deck import Deck
from card import Card
from players import BlackJackPlayer, HumBlackJackPlayer
from random import randint

class BlackJackManager:

    COMPNAMES = ["Angela", "Chelsea", "Daryl", "Elizabeth", "Fred", "Gabby",
                 "Harold", "Irene", "Julie", "Katie", "Lindsey", "Mike",
                 "Nancy", "Oliver", "Pat", "Richard", "Samantha", "Terrence",
                 "Ursula", "Vic", "Wendy", "Xavier", "Yanni", "Zach"]

    def __init__(self):
        self.deck = Deck()
        self.players = []


    def reset(self):
        self.dealer = BlackJackPlayer()
        self.deck.shuffle()
        print("")
        print("Enter your name:")
        playerName = input(" --> ")
        self.players.append(HumBlackJackPlayer(playerName))
        
        for _ in range(2):
            nameIdx = randint(0, len(self.COMPNAMES) - 1)
            newComp = BlackJackPlayer(self.COMPNAMES[nameIdx])
            self.players.append(newComp)

        self.players.append(self.dealer)
        self.starterDeal()


    def starterDeal(self):
        for _ in range(2):
            for player in self.players:
                player.draw(self.deck.draw())


    def manageTurn(self, player):
        takingTurn = True
        while takingTurn:
            playerChoice = player.chooseAction()
            if playerChoice == "hit":
                player.draw(self.deck.draw())
            elif playerChoice == "win":
                chance = randint(0, 100)
                if chance <= 30:
                    # We get caught
                    print("")
                    print("You got caught cheating!")
                    print("")
                    player.score = 50
                else:
                    for idx in range(len(player.hand)):
                        player.discard(0)
                    player.draw(Card("Ace", "Spades"))
                    player.draw(Card("Queen", "Hearts"))   
                takingTurn = False
            else:
                takingTurn = False


    def determineWinners(self):
        highScore = 0
        for player in self.players:
            if player.score > highScore and player.score <= 21:
                highScore = player.score
        winners = []
        for player in self.players:
            if player.score == highScore:
                winners.append(player)
        
        if len(winners) == 0:
            print("Nobody wins! Everyone busts!")
        elif len(winners) == 1:
            print(f"{winners[0]} wins with a score of {highScore}!")
        elif self.dealer in winners:
            print(f"{self.dealer} wins with a score of {highScore}!")
        elif len(winners) == 2:
            print(f"{winners[0]} and {winners[1]} both win with a score of {highScore}!")
        else:
            winnerNames = ""
            for idx in range(len(winners) - 1):
                winnerNames += f"{winners[idx]}"
                if idx == len(winners) - 2:
                    winnerNames += ", and "
                else:
                    winnerNames += ", "
            print(f"{winnerNames} win with a score of {highScore}!")


    def promptNextGame(self):
        print("")
        print("Would you like to play another game of blackjack? (y/n)")
        playAgain = input(" --> ").lower()
        if playAgain in ["yes", "y", "sure"]:
            return True
        else:
            return False


    def playGame(self):
        gameOn = True
        while gameOn:
            for _ in range(50):
                print("")
            print("~~~~~ WELCOME TO BLACKJACK! ~~~~~")

            self.reset()

            for player in self.players:
                self.manageTurn(player)

            for player in self.players:
                player.showHand()

            self.determineWinners()

            gameOn = self.promptNextGame()

            if gameOn == False:
                for _ in range(50):
                    print("")

    
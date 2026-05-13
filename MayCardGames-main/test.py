from card import Card
from deck import Deck
from players import HumBlackJackPlayer

def main():
    testDeck = Deck()

    testPlayer = HumBlackJackPlayer()

    for _ in range(2):
        testPlayer.draw(testDeck.draw())

    testPlayer.showHand()

    move = ""
    while move != "stay":
        move = testPlayer.chooseAction()
        if move == "hit":
            testPlayer.draw(testDeck.draw())




main()
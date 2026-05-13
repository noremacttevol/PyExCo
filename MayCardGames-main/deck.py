from card import Card
from random import shuffle

class Deck:
    
    RANKS = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    SUITS = ["Clubs", "Diamonds", "Spades", "Hearts"]

    def __init__(self, numDecks=1):
        self.numDecks = numDecks
        self.reset()


    def reset(self):
        self.drawPile = []
        self.discardPile = []
        self.outPile = []
        for _ in range(self.numDecks):
            for suit in self.SUITS:
                for rank in self.RANKS:
                    newCard = Card(rank, suit)
                    self.drawPile.append(newCard)
        

    def shuffle(self):
        shuffle(self.drawPile)


    def draw(self):
        toReturn = self.drawPile.pop(0)
        self.outPile.append(toReturn)
        return toReturn


    def discard(self, toDiscard):
        if toDiscard in self.outPile:
            self.outPile.remove(toDiscard)
        self.discardPile.append(toDiscard)


    def __repr__(self):
        # return f"A deck comprised of {self.numDecks} standard decks"
        return "\n".join(str(card) for card in self.drawPile)


    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if len(self.drawPile) != len(other.drawPile):
            return False
        if len(self.discardPile) != len(other.discardPile):
            return False
        if len(self.outPile) != len(other.outPile):
            return False
        for idx in range(len(self.drawPile)):
            if self.drawPile[idx] != other.drawPile[idx]:
                return False
        for idx in range(len(self.discardPile)):
            if self.discardPile[idx] != other.discardPile[idx]:
                return False
        for idx in range(len(self.outPile)):
            if self.outPile[idx] != other.outPile[idx]:
                return False
        return True
    
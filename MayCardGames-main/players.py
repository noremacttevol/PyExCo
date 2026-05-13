class BlackJackPlayer:
    
    VALUES = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
              "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

    def __init__(self, name="Bob", difficulty="norm"):
        self.name = name
        self.difficulty = difficulty
        self.hand = []
        self.score = 0


    def draw(self, drawnCard):
        self.hand.append(drawnCard)


    def discard(self, cardIdx):
        return self.hand.pop(cardIdx)


    def showHand(self):
        print("")
        print(f"~~~~~ {self.name}'s Hand ~~~~~")
        print("")
        if len(self.hand) > 0:
            for idx in range(len(self.hand)):
                print(f"{idx+1}. {self.hand[idx]}")
        else:
            print("No cards in hand!")
        print("")


    def calcScore(self):
        self.score = 0
        aces = 0
        if len(self.hand) > 0:
            for card in self.hand:
                self.score += self.VALUES[card.rank]
                if card.rank == "Ace":
                    aces += 1
            while self.score > 21 and aces > 0:
                self.score -= 10
                aces -= 1


    def chooseAction(self):
        self.calcScore()
        if self.score >= 17 or len(self.hand) >= 5:
            return "stay"
        else:
            return "hit"


    def __repr__(self):
        return f"{self.name}"
    

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.name != other.name:
            return False
        if self.difficulty != other.difficulty:
            return False
        if len(self.hand) != len(other.hand):
            return False
        for idx in range(len(self.hand)):
            if self.hand[idx] != other.hand[idx]:
                return False
        return True


class HumBlackJackPlayer(BlackJackPlayer):
    
    def chooseAction(self):
        self.calcScore()
        if self.score >= 21 or len(self.hand) >= 5:
            return "stay"
        else:
            validChoice = False
            while not validChoice:
                self.showHand()
                print("Would you like to 'hit' or 'stay'?")
                playerChoice = input(" --> ").lower()
                if playerChoice in ['hit', 'h']:
                    playerChoice = "hit"
                    validChoice = True
                elif playerChoice in ['stay', 's']:
                    playerChoice = "stay"
                    validChoice = True
                elif playerChoice in ['cheat', 'win', 'w', 'c']:
                    playerChoice = "win"
                    validChoice = True
                else:
                    print("That's not a valid move - try again!")
            return playerChoice

# card.py
# Represents one playing card. Has a rank (like "Ace") and a suit (like "Spades")
# and a numeric value so we can do math on it when scoring hands.
# I built this the same way Daniel built his Card class for the blackjack demo.

class Card:

    # This is a class-level dictionary — it belongs to the Card class, not any
    # one specific card. It maps rank names to numbers so we can compare cards.
    RANK_VALUES = {
        "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
        "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
        "Jack": 11, "Queen": 12, "King": 13, "Ace": 14
    }

    def __init__(self, rank="Two", suit="Clubs"):
        self.rank = rank
        self.suit = suit
        # Look up the numeric value for this rank from the dictionary above
        self.value = self.RANK_VALUES[rank]

    # __repr__ controls what you see when you print a card object
    def __repr__(self):
        return f"[{self.rank} of {self.suit}]"

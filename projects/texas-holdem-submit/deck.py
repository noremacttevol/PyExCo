# deck.py
# Represents a standard 52-card deck. Can be shuffled and cards can be dealt.
# I modeled this closely after Daniel's Deck class from the card game demo.

from card import Card
from random import shuffle


class Deck:

    # All 13 ranks and 4 suits — class-level constants
    RANKS = [
        "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
        "Nine", "Ten", "Jack", "Queen", "King", "Ace"
    ]
    SUITS = ["Clubs", "Diamonds", "Spades", "Hearts"]

    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        """Rebuild a fresh shuffled deck — called at the start of each new hand."""
        # Build all 52 cards using nested loops (one for each suit, one for each rank)
        self.cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(Card(rank, suit))
        shuffle(self.cards)

    def deal(self):
        """Remove and return the top card from the deck."""
        return self.cards.pop()

    def __repr__(self):
        return f"Deck with {len(self.cards)} cards remaining"

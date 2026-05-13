# ── DECK CLASS ──────────────────────────────────────────────────────────────
# Standard 52-card deck. Can shuffle and deal one card at a time.
# reset() rebuilds all 52 cards — call this at the start of each new hand.

from card import Card
from random import shuffle


class Deck:

    RANKS = [
        "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
        "Nine", "Ten", "Jack", "Queen", "King", "Ace"
    ]
    SUITS = ["Clubs", "Diamonds", "Spades", "Hearts"]

    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        """Rebuild and shuffle a fresh 52-card deck."""
        self.cards = [Card(rank, suit) for suit in self.SUITS for rank in self.RANKS]
        shuffle(self.cards)

    def deal(self):
        """Pop and return the top card. Crashes if deck is empty — shouldn't happen in normal play."""
        return self.cards.pop()

    def cards_remaining(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck ({len(self.cards)} cards remaining)"

# ── CARD CLASS ──────────────────────────────────────────────────────────────
# One card. Has a rank (Two through Ace) and a suit (Clubs/Diamonds/Spades/Hearts).
# Also carries a numeric value (2-14) so the hand evaluator can do math on it.

class Card:

    # Lookup table: rank name → numeric value
    # Ace = 14 (high). Ace-low (wheel straight) is handled in hand_evaluator.
    RANK_VALUES = {
        "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
        "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
        "Jack": 11, "Queen": 12, "King": 13, "Ace": 14
    }

    def __init__(self, rank="Two", suit="Clubs"):
        self.rank = rank
        self.suit = suit
        self.value = self.RANK_VALUES[rank]

    # What prints when you print(card) or put it in a list print
    def __repr__(self):
        return f"[{self.rank} of {self.suit}]"

    # What prints in an f-string or str()
    def __str__(self):
        return f"{self.rank} of {self.suit}"

    # Allows == comparison between two Card objects
    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit

    # Allows < comparison (used for sorting)
    def __lt__(self, other):
        return self.value < other.value

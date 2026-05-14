# players.py
# Defines the player classes using inheritance — same concept Daniel showed
# with BlackJackPlayer and HumBlackJackPlayer.
#
# CmpPlayer = the base class (computer player behavior by default)
# HmnPlayer = child class — overrides the action method to take keyboard input
# The game manager can loop through all players and call .decide_action() on each
# without caring which type they are. That's the polymorphism part.


class CmpPlayer:
    """Base player class — behaves as a computer opponent."""

    def __init__(self, name, chips=1000):
        self.name    = name
        self.chips   = chips
        self.hand    = []       # This player's hole cards (2 cards)
        self.folded  = False
        self.score   = 0        # Hand score set during evaluation
        self.hand_name = ""     # Human-readable hand name (e.g. "Two Pair")

    def receive_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        """Reset for a new hand."""
        self.hand      = []
        self.folded    = False
        self.score     = 0
        self.hand_name = ""

    def show_hand(self):
        print(f"\n  {self.name}'s cards:")
        for card in self.hand:
            print(f"    {card}")
        if self.hand_name:
            print(f"    Best hand: {self.hand_name}")

    def decide_action(self, community_cards):
        """
        Computer AI: look at hole cards and decide fold/call/raise.
        Simple strategy — good enough to demonstrate the concept.
        """
        if len(self.hand) < 2:
            return "call"

        v1 = self.hand[0].value
        v2 = self.hand[1].value
        is_pair = (v1 == v2)
        high_card = max(v1, v2)

        # Raise with premium hands
        if is_pair and high_card >= 10:
            return "raise"
        # Call with decent hands
        if is_pair or high_card >= 12:
            return "call"
        # Fold weak hands (check for free if possible)
        return "fold"

    def __repr__(self):
        return f"{self.name} (${self.chips})"


class HmnPlayer(CmpPlayer):
    """
    Human player — inherits everything from CmpPlayer.
    Only overrides decide_action so the player gets to type their choice.
    """

    def decide_action(self, community_cards):
        """Show the player their hand and ask what they want to do."""
        self.show_hand()

        if community_cards:
            print(f"\n  Community cards: {' '.join(str(c) for c in community_cards)}")

        while True:
            choice = input("\n  Your action (fold / call / raise): ").lower().strip()
            if choice in ["fold", "f"]:
                return "fold"
            elif choice in ["call", "c", "check"]:
                return "call"
            elif choice in ["raise", "r", "bet", "b"]:
                return "raise"
            else:
                print("  Type fold, call, or raise.")

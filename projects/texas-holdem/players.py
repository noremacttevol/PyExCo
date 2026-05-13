# ── PLAYER CLASSES ──────────────────────────────────────────────────────────
# PokerPlayer        — base class (computer player behavior built in)
# HumanPokerPlayer   — subclass, overrides decide_action() to ask the user
# ComputerPokerPlayer — subclass, overrides decide_action() with AI strategy
#
# Polymorphism in action: the game manager calls player.decide_action() on
# every player in the list without knowing or caring which type it is.
# Python calls the right version based on the object's actual class.

from hand_evaluator import HandEvaluator


class PokerPlayer:
    """Base class — represents a computer player with a simple strategy."""

    def __init__(self, name, chips=1000):
        self.name   = name
        self.chips  = chips
        self.hand   = []          # Hole cards (2 cards)
        self.folded = False
        self.current_bet    = 0   # Amount bet in the current betting round
        self.best_hand_score = None
        self.best_hand_name  = ""

    def receive_card(self, card):
        self.hand.append(card)

    def clear_for_new_hand(self):
        self.hand          = []
        self.folded        = False
        self.current_bet   = 0
        self.best_hand_score = None
        self.best_hand_name  = ""

    def show_hand(self, hide=False):
        """Print this player's hole cards. hide=True shows face-down cards."""
        if hide:
            print(f"\n  {self.name}: [**] [**]")
        else:
            cards_str = "  ".join(str(c) for c in self.hand)
            print(f"\n  {self.name}: {cards_str}")
            if self.best_hand_name:
                print(f"    → {self.best_hand_name}")

    def decide_action(self, current_bet, pot, community_cards):
        """
        Computer AI strategy.
        Pre-flop: play tight — only strong hole cards.
        Post-flop: evaluate current hand strength vs the board.
        Returns: "fold" | "call" | "raise"
        """
        to_call = current_bet - self.current_bet

        # Post-flop: can evaluate actual hand
        if len(community_cards) >= 3 and len(self.hand) == 2:
            score, name, _ = HandEvaluator.best_hand(self.hand, community_cards)
            hand_rank = score[0]   # 0=high card ... 8=straight flush

            if hand_rank >= 5:        # Flush or better → raise
                return "raise"
            elif hand_rank >= 3:      # Three of a kind or better → call
                return "call"
            elif hand_rank == 2:      # Two pair → call if cheap
                return "call" if to_call <= self.chips * 0.25 else "fold"
            else:                     # Pair or worse → fold if it costs anything
                return "call" if to_call == 0 else "fold"

        # Pre-flop: decide based on hole card strength only
        if len(self.hand) == 2:
            v1 = self.hand[0].value
            v2 = self.hand[1].value
            high = max(v1, v2)
            low  = min(v1, v2)
            is_pair = (v1 == v2)

            if is_pair and high >= 10:       # High pocket pair (TT+) → raise
                return "raise"
            elif is_pair:                    # Low pocket pair → call
                return "call"
            elif high == 14 and low >= 10:   # Ace + high card → raise
                return "raise"
            elif high >= 12:                 # King/Queen with anything → call
                return "call"
            else:                            # Weak hand → fold if costs anything
                return "call" if to_call == 0 else "fold"

        return "call"   # Safety fallback

    def __repr__(self):
        status = " (folded)" if self.folded else ""
        return f"{self.name} (${self.chips}){status}"


# ─────────────────────────────────────────────────────────────────────────────

class HumanPokerPlayer(PokerPlayer):
    """Human player — overrides decide_action to get input from the keyboard."""

    def decide_action(self, current_bet, pot, community_cards):
        to_call = current_bet - self.current_bet

        while True:
            print(f"\n  Your chips : ${self.chips}")
            print(f"  Pot        : ${pot}")
            if to_call > 0:
                print(f"  To call    : ${to_call}")
            else:
                print(f"  (You can check for free)")

            raw = input("  Action (fold / call / raise): ").lower().strip()

            if raw in ["fold", "f"]:
                return "fold"
            elif raw in ["call", "call it", "c", "check", "ch"]:
                return "call"
            elif raw in ["raise", "r", "bet", "b"]:
                return "raise"
            else:
                print("  Type: fold, call, or raise")


# ─────────────────────────────────────────────────────────────────────────────

class ComputerPokerPlayer(PokerPlayer):
    """
    Computer player with slightly more aggressive strategy than the base class.
    Inherits everything from PokerPlayer, only overrides decide_action.
    Same concept as Daniel's HumBlackJackPlayer inheriting from BlackJackPlayer.
    """

    def decide_action(self, current_bet, pot, community_cards):
        """More aggressive than base — raises more frequently with strong hands."""
        to_call = current_bet - self.current_bet

        if len(community_cards) >= 3 and len(self.hand) == 2:
            score, name, _ = HandEvaluator.best_hand(self.hand, community_cards)
            hand_rank = score[0]

            if hand_rank >= 6:        # Full house or better → always raise
                return "raise"
            elif hand_rank >= 4:      # Straight or flush → raise
                return "raise"
            elif hand_rank >= 2:      # Two pair / three of a kind → call
                return "call"
            else:
                return "call" if to_call == 0 else "fold"

        # Pre-flop
        if len(self.hand) == 2:
            v1 = self.hand[0].value
            v2 = self.hand[1].value
            is_pair = (v1 == v2)
            high = max(v1, v2)

            if is_pair and high >= 8:       # 8s or better → raise
                return "raise"
            elif is_pair:
                return "call"
            elif high == 14:                # Any Ace → raise
                return "raise"
            elif high >= 11:               # Jack or better → call
                return "call"
            else:
                return "call" if to_call == 0 else "fold"

        return "call"

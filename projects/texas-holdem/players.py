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

    def decide_action(self, community_cards, current_bet=0, to_call=0, min_raise=50):
        """
        Computer AI strategy.
        Post-flop: evaluate hand strength with HandEvaluator.
        Pre-flop: simple hole-card strength rules.
        Returns: "fold" | "call" | "check" | "raise"
        """
        # Post-flop: evaluate actual hand against the board
        if len(community_cards) >= 3 and len(self.hand) == 2:
            score, name, _ = HandEvaluator.best_hand(self.hand, community_cards)
            hand_rank = score[0]   # 0=high card … 8=straight flush

            if hand_rank >= 5:    # Flush or better → raise
                return "raise"
            elif hand_rank >= 3:  # Three of a kind or better → call/check
                return "call" if to_call > 0 else "check"
            elif hand_rank == 2:  # Two pair → call if cheap
                return ("call" if to_call <= self.chips * 0.25 else "fold") if to_call > 0 else "check"
            else:                 # Pair or worse → check for free, else fold
                return "check" if to_call == 0 else "fold"

        # Pre-flop: decide on hole card strength only
        if len(self.hand) == 2:
            v1      = self.hand[0].value
            v2      = self.hand[1].value
            is_pair = (v1 == v2)
            high    = max(v1, v2)

            if is_pair and high >= 10:
                return "raise"
            elif is_pair or high >= 12:
                return "call" if to_call > 0 else "check"
            else:
                return "fold" if to_call > 0 else "check"

        return "check" if to_call == 0 else "call"

    def __repr__(self):
        status = " (folded)" if self.folded else ""
        return f"{self.name} (${self.chips}){status}"


# ─────────────────────────────────────────────────────────────────────────────

class HumanPokerPlayer(PokerPlayer):
    """Human player — overrides decide_action to get input from the keyboard."""

    def decide_action(self, community_cards, current_bet=0, to_call=0, min_raise=50):
        while True:
            print(f"\n  Your chips : ${self.chips}")
            if to_call > 0:
                print(f"  Current bet: ${current_bet}   Your cost to call: ${to_call}")
                raw = input("  Action (fold / call / raise [amount]): ").lower().strip()
            elif current_bet > 0:
                # BB option: already covered the big blind, no raise yet
                print(f"  No raise yet — you are covered.")
                raw = input("  Action (check / raise [amount] / fold): ").lower().strip()
            else:
                print(f"  No bet yet — you can check for free.")
                raw = input("  Action (check / raise [amount] / fold): ").lower().strip()

            parts = raw.split(None, 1)
            verb  = parts[0] if parts else ""
            rest  = parts[1] if len(parts) > 1 else ""

            if verb in ["fold", "f"]:
                return "fold"
            elif verb in ["call", "call it", "c"]:
                return "call"
            elif verb in ["check", "ch"]:
                if to_call > 0:
                    print(f"  Can't check — there's ${to_call} to call. Fold, call, or raise.")
                else:
                    return "call"
            elif verb in ["raise", "r", "bet", "b"]:
                amount = self._parse_raise(rest, min_raise)
                if amount is not None:
                    return ("raise", amount)
            else:
                print("  Type fold, call, or raise." if to_call > 0 else "  Type check, raise, or fold.")

    def _parse_raise(self, rest, min_raise):
        """Parse a raise amount from inline text, or prompt if not provided."""
        capped_min = min(min_raise, self.chips)
        if rest:
            raw = rest.replace("$", "").strip()
            if raw in ["all", "allin", "all-in"]:
                return self.chips
            try:
                amount = int(raw)
                if capped_min <= amount <= self.chips:
                    return amount
                print(f"  Must be between ${capped_min} and ${self.chips}.")
            except ValueError:
                print("  Enter a number or 'all'.")
            return None
        else:
            while True:
                raw = input(f"  Raise by how much? (${capped_min}–${self.chips}, or 'all'): ").lower().strip()
                if raw in ["all", "allin", "all-in"]:
                    return self.chips
                try:
                    amount = int(raw)
                    if capped_min <= amount <= self.chips:
                        return amount
                    print(f"  Must be between ${capped_min} and ${self.chips}.")
                except ValueError:
                    print("  Enter a number or 'all'.")


# ─────────────────────────────────────────────────────────────────────────────

class ComputerPokerPlayer(PokerPlayer):
    """
    Computer player with slightly more aggressive strategy than the base class.
    Inherits everything from PokerPlayer, only overrides decide_action.
    Same concept as Daniel's HumBlackJackPlayer inheriting from BlackJackPlayer.
    """

    def decide_action(self, community_cards, current_bet=0, to_call=0, min_raise=50):
        """More aggressive than base — raises more frequently with strong hands."""
        # Post-flop: use hand evaluator
        if len(community_cards) >= 3 and len(self.hand) == 2:
            score, name, _ = HandEvaluator.best_hand(self.hand, community_cards)
            hand_rank = score[0]

            if hand_rank >= 6:    # Full house or better → raise
                return "raise"
            elif hand_rank >= 4:  # Straight or flush → raise
                return "raise"
            elif hand_rank >= 2:  # Two pair / three of a kind → call/check
                return "call" if to_call > 0 else "check"
            else:
                return "check" if to_call == 0 else "fold"

        # Pre-flop: more aggressive thresholds
        if len(self.hand) == 2:
            v1      = self.hand[0].value
            v2      = self.hand[1].value
            is_pair = (v1 == v2)
            high    = max(v1, v2)

            if is_pair and high >= 8:    # 8s or better → raise
                return "raise"
            elif is_pair:
                return "call" if to_call > 0 else "check"
            elif high == 14:             # Any Ace → raise
                return "raise"
            elif high >= 11:             # Jack or better → call/check
                return "call" if to_call > 0 else "check"
            else:
                return "fold" if to_call > 0 else "check"

        return "check" if to_call == 0 else "call"

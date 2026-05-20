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

    def decide_action(self, community_cards, current_bet=0, to_call=0, min_raise=50):
        """
        Computer AI: look at hole cards and decide what to do.
        If there's no bet (to_call == 0), check for free on weak hands instead of folding.
        """
        if len(self.hand) < 2:
            return "check" if to_call == 0 else "call"

        v1 = self.hand[0].value
        v2 = self.hand[1].value
        is_pair   = (v1 == v2)
        high_card = max(v1, v2)

        # Premium hands: always raise
        if is_pair and high_card >= 10:
            return "raise"
        # Decent hands: call a bet, or check for free
        if is_pair or high_card >= 12:
            return "call" if to_call > 0 else "check"
        # Weak hands: fold if there's a bet, otherwise check for free
        return "fold" if to_call > 0 else "check"

    def __repr__(self):
        return f"{self.name} (${self.chips})"


class HmnPlayer(CmpPlayer):
    """
    Human player — inherits everything from CmpPlayer.
    Only overrides decide_action so the player gets to type their choice.
    """

    def decide_action(self, community_cards, current_bet=0, to_call=0, min_raise=50):
        """Show the player their hand and ask what they want to do."""
        self.show_hand()

        if community_cards:
            print(f"\n  Community cards: {' '.join(str(c) for c in community_cards)}")

        if to_call > 0:
            print(f"\n  Current bet: ${current_bet}   Your cost to call: ${to_call}")
            prompt = "\n  fold / call / raise (f/c/r): "
        elif current_bet > 0:
            print(f"\n  No raise yet — you're covered. Check or raise?")
            prompt = "\n  check / raise / fold (c/r/f): "
        else:
            print(f"\n  No bet yet — you can check for free.")
            prompt = "\n  check / raise / fold (c/r/f): "

        while True:
            choice = input(prompt).lower().strip()
            words  = choice.split()
            verb   = words[0] if words else ""
            rest   = words[1].lstrip("$") if len(words) > 1 else ""

            if not verb:
                continue

            if verb in ["fold", "f"]:
                return "fold"

            elif verb in ["call", "c"]:
                if to_call > 0:
                    return "call"
                return "check"  # "c" doubles as check when there's no bet

            elif verb in ["check", "ch", "x"]:
                if to_call == 0:
                    return "check"
                print(f"  Can't check — there's ${to_call} to call (f/c/r).")

            elif verb in ["raise", "r", "bet", "b"]:
                eff_min = min(min_raise, self.chips)

                # Accept inline amount: "raise 450" or "raise $450" or just "raise"
                if rest:
                    if rest in ["all", "a", "allin"]:
                        return ("raise", self.chips)
                    try:
                        val = int(rest)
                        if val < eff_min:
                            print(f"  Minimum raise is ${eff_min}.")
                        elif val > self.chips:
                            print(f"  You only have ${self.chips}.")
                        else:
                            return ("raise", val)
                        continue
                    except ValueError:
                        print(f"  '{rest}' is not a number. Try: raise 200")
                        continue

                # No inline amount — prompt on the next line
                print(f"  You have ${self.chips}. Raise by how much? (min ${eff_min}, or 'all' to go all-in)")
                while True:
                    raw = input("  Raise by $").strip().lower().lstrip("$")
                    if raw in ["all", "a", "allin"]:
                        return ("raise", self.chips)
                    try:
                        amount = int(raw)
                    except ValueError:
                        print("  Enter a number (or 'all').")
                        continue
                    if amount < eff_min:
                        print(f"  Minimum raise is ${eff_min}.")
                    elif amount > self.chips:
                        print(f"  You only have ${self.chips}.")
                    else:
                        return ("raise", amount)

            else:
                if to_call > 0:
                    print("  Type fold, call, or raise  (f/c/r) — e.g. raise 200")
                else:
                    print("  Type check, raise, or fold  (c/r/f) — e.g. raise 200")

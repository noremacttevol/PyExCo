# holdem_manager.py
# The TexasHoldemManager class controls the whole game.
# It handles: dealing, betting rounds, evaluating hands, finding the winner.
# This is the equivalent of Daniel's BlackJackManager — the brain of the operation.

from deck import Deck
from players import PokerPlayer, HumanPokerPlayer
from random import choice as rand_choice


class TexasHoldemManager:

    # Computer player name pool
    COMP_NAMES = ["Angela", "Brett", "Carlos", "Diana", "Eddie", "Fiona"]

    # Blind amounts
    SMALL_BLIND = 25
    BIG_BLIND   = 50

    def __init__(self):
        self.deck            = Deck()
        self.players         = []
        self.community_cards = []
        self.pot             = 0

    # ── HAND EVALUATION ──────────────────────────────────────────────────────
    # I wrote this to work on all 7 cards at once (2 hole + 5 community).
    # It checks for each hand type from best to worst and returns the first match.

    def evaluate_hand(self, hole_cards, community_cards):
        """
        Look at all 7 cards and return (score, hand_name).
        Higher score = better hand.
        """
        all_cards = hole_cards + community_cards
        values    = sorted([c.value for c in all_cards], reverse=True)
        suits     = [c.suit for c in all_cards]

        # Count how many of each value we have
        value_counts = {}
        for v in values:
            value_counts[v] = value_counts.get(v, 0) + 1

        # Sort counts so the highest count is first
        counts = sorted(value_counts.values(), reverse=True)

        # Check for flush — 5 or more cards of the same suit
        suit_counts = {}
        for s in suits:
            suit_counts[s] = suit_counts.get(s, 0) + 1
        has_flush = any(count >= 5 for count in suit_counts.values())

        # Check for straight — any 5 consecutive values in the hand
        unique_values = sorted(set(values), reverse=True)
        has_straight  = False
        straight_high = 0

        for i in range(len(unique_values) - 4):
            if unique_values[i] - unique_values[i + 4] == 4:
                has_straight  = True
                straight_high = unique_values[i]
                break

        # Ace-low straight: A-2-3-4-5
        if not has_straight and set([14, 2, 3, 4, 5]).issubset(set(values)):
            has_straight  = True
            straight_high = 5

        # Determine hand type (best to worst)
        if has_straight and has_flush:
            return 8, "Straight Flush"
        if counts[0] == 4:
            return 7, "Four of a Kind"
        if counts[0] == 3 and len(counts) > 1 and counts[1] >= 2:
            return 6, "Full House"
        if has_flush:
            return 5, "Flush"
        if has_straight:
            return 4, "Straight"
        if counts[0] == 3:
            return 3, "Three of a Kind"
        if counts[0] == 2 and len(counts) > 1 and counts[1] == 2:
            return 2, "Two Pair"
        if counts[0] == 2:
            return 1, "One Pair"

        # High card — use the highest card value as a tiebreaker
        return 0, "High Card"

    # ── SETUP ────────────────────────────────────────────────────────────────

    def setup_players(self):
        name = input("Enter your name: ").strip() or "Player"
        self.players = [HumanPokerPlayer(name, chips=1000)]

        used_names = []
        for _ in range(3):
            available = [n for n in self.COMP_NAMES if n not in used_names]
            comp_name = rand_choice(available)
            used_names.append(comp_name)
            self.players.append(PokerPlayer(comp_name, chips=1000))

        print("\nPlayers at the table:")
        for p in self.players:
            print(f"  {p.name} — ${p.chips}")

    # ── DEALING ──────────────────────────────────────────────────────────────

    def deal_hole_cards(self):
        """Deal 2 cards to each player."""
        for _ in range(2):
            for player in self.players:
                player.receive_card(self.deck.deal())

    def deal_community_cards(self, count):
        """Deal cards to the shared community."""
        for _ in range(count):
            self.community_cards.append(self.deck.deal())

    # ── BETTING ROUND ────────────────────────────────────────────────────────

    def betting_round(self, round_name):
        """
        Run one betting round. Each active player decides: fold, call, or raise.
        Pot grows with each call or raise.
        """
        print(f"\n  --- {round_name} ---")
        if self.community_cards:
            print(f"  Board: {' '.join(str(c) for c in self.community_cards)}")
        print(f"  Pot: ${self.pot}")

        for player in self.players:
            if player.folded:
                continue

            action = player.decide_action(self.community_cards)

            if action == "fold":
                player.folded = True
                print(f"  {player.name} folds.")
            elif action == "call":
                amount = self.BIG_BLIND
                if amount <= player.chips:
                    player.chips -= amount
                    self.pot     += amount
                print(f"  {player.name} calls (${amount} into pot).")
            elif action == "raise":
                amount = self.BIG_BLIND * 2
                if amount <= player.chips:
                    player.chips -= amount
                    self.pot     += amount
                print(f"  {player.name} raises (${amount} into pot).")

    # ── SHOWDOWN ─────────────────────────────────────────────────────────────

    def showdown(self):
        """Evaluate all remaining hands and find the winner."""
        print("\n  ===== SHOWDOWN =====")
        print(f"  Final board: {' '.join(str(c) for c in self.community_cards)}")

        active_players = [p for p in self.players if not p.folded]

        for player in active_players:
            score, name   = self.evaluate_hand(player.hand, self.community_cards)
            player.score      = score
            player.hand_name  = name
            player.show_hand()

        # Winner = highest score
        winner = max(active_players, key=lambda p: p.score)
        return winner

    # ── FULL HAND FLOW ────────────────────────────────────────────────────────

    def play_hand(self):
        """Run one complete hand from deal to showdown."""
        # Reset everything for a new hand
        self.community_cards = []
        self.pot             = 0
        self.deck.reset()
        for player in self.players:
            player.clear_hand()

        print("\n" + "="*40)
        print("  NEW HAND")
        print("="*40)

        # Blinds
        if len(self.players) >= 2:
            self.players[1].chips -= self.SMALL_BLIND
            self.pot              += self.SMALL_BLIND
            self.players[0].chips -= self.BIG_BLIND
            self.pot              += self.BIG_BLIND
            print(f"  {self.players[1].name} posts small blind (${self.SMALL_BLIND})")
            print(f"  {self.players[0].name} posts big blind (${self.BIG_BLIND})")

        # Deal hole cards
        self.deal_hole_cards()

        # Pre-Flop betting
        self.betting_round("Pre-Flop")

        active = [p for p in self.players if not p.folded]
        if len(active) == 1:
            winner = active[0]
        else:
            # Flop (3 cards)
            self.deal_community_cards(3)
            self.betting_round("Flop")
            active = [p for p in self.players if not p.folded]

            if len(active) == 1:
                winner = active[0]
            else:
                # Turn (1 card)
                self.deal_community_cards(1)
                self.betting_round("Turn")
                active = [p for p in self.players if not p.folded]

                if len(active) == 1:
                    winner = active[0]
                else:
                    # River (1 card)
                    self.deal_community_cards(1)
                    self.betting_round("River")
                    active = [p for p in self.players if not p.folded]

                    if len(active) == 1:
                        winner = active[0]
                    else:
                        winner = self.showdown()

        # Award the pot
        winner.chips += self.pot
        print(f"\n  *** {winner.name} wins the pot of ${self.pot}! ***")
        if winner.hand_name:
            print(f"      (Winning hand: {winner.hand_name})")

    # ── GAME SESSION ──────────────────────────────────────────────────────────

    def play_game(self):
        """Full game session — play hands until someone is broke or player quits."""
        self.setup_players()

        game_on = True
        while game_on:
            self.play_hand()

            # Remove any player who ran out of chips
            self.players = [p for p in self.players if p.chips > 0]

            if len(self.players) == 1:
                print(f"\n  Game over! {self.players[0].name} wins everything!")
                game_on = False
                break

            # Show chip counts
            print("\n  Chip counts:")
            for p in self.players:
                print(f"    {p.name}: ${p.chips}")

            again = input("\n  Play another hand? (y/n): ").strip().lower()
            if again not in ["y", "yes"]:
                game_on = False

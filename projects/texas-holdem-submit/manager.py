# manager.py
# The TexasHoldemManager class controls the whole game.
# It handles: dealing, betting rounds, evaluating hands, finding the winner.
# This is the equivalent of Daniel's BlackJackManager — the brain of the operation.
#
# I picked Texas Hold'em because I like the movie Tombstone.
# Doc Holliday plays poker in it. Seemed like the right call.

import json
import os

from deck import Deck
from players import CmpPlayer, HmnPlayer
from random import choice as rand_choice


class TexasHoldemManager:

    # Computer player name pool — pulled from Tombstone character names for fun
    COMP_NAMES = ["Doc", "Virgil", "Morgan", "Wyatt", "Turkey Creek", "Texas Jack"]
    SAVE_FILE  = "holdem_save.json"

    # Blind amounts
    SMALL_BLIND = 25
    BIG_BLIND   = 50

    # Tombstone lines for when someone folds and leaves the table
    FOLD_QUOTES = [
        "Well... bye.",
        "It appears the strain was more than he could bear.",
        "He's gone to his reward.",
        "Are you gonna do something or just stand there and bleed?",
    ]

    def __init__(self):
        self.deck            = Deck()
        self.players         = []
        self.community_cards = []
        self.pot             = 0
        self.btn_idx         = 0  # index of the dealer/button — advances each hand

    # ── SAVE / LOAD ───────────────────────────────────────────────────────────

    def save_game(self):
        """Write chip counts, player names, and button position to a JSON file."""
        state = {
            "btn_idx": self.btn_idx,
            "players": [
                {"name": p.name, "chips": p.chips, "human": isinstance(p, HmnPlayer)}
                for p in self.players
            ],
        }
        with open(self.SAVE_FILE, "w") as f:
            json.dump(state, f)
        print("  Game saved.  'I'll be your huckleberry.' — See you next time.")

    def load_game(self):
        """Load a saved game, delete the file, and return True. Returns False if no save exists."""
        if not os.path.exists(self.SAVE_FILE):
            return False
        with open(self.SAVE_FILE) as f:
            state = json.load(f)
        self.btn_idx = state["btn_idx"]
        self.players = [
            HmnPlayer(p["name"], chips=p["chips"]) if p["human"]
            else CmpPlayer(p["name"], chips=p["chips"])
            for p in state["players"]
        ]
        os.remove(self.SAVE_FILE)
        return True

    # ── HAND EVALUATION ──────────────────────────────────────────────────────
    # Works on all 7 cards at once (2 hole + 5 community).
    # Checks for each hand type from best to worst and returns the first match.

    def evaluate_hand(self, hole_cards, community_cards):
        """
        Score all 7 cards and return (score_tuple, hand_name).
        score_tuple is compared element-by-element, so tiebreakers work automatically.
        e.g. pair of Queens beats pair of 7s: (1,12,14,13,8) > (1,7,14,13,8)
        """
        all_cards = hole_cards + community_cards
        values    = sorted([c.value for c in all_cards], reverse=True)

        # Group cards by suit for flush / straight-flush detection
        by_suit = {}
        for c in all_cards:
            by_suit.setdefault(c.suit, []).append(c.value)

        # Sort each value by (count desc, value desc) — determines hand type + tiebreakers
        val_count = {}
        for v in values:
            val_count[v] = val_count.get(v, 0) + 1
        ranked = sorted(val_count.items(), key=lambda x: (x[1], x[0]), reverse=True)
        rv = [v for v, _ in ranked]   # values in priority order
        rc = [c for _, c in ranked]   # their counts

        # Flush: 5+ cards of one suit
        flush_vals = None
        for suit_vals in by_suit.values():
            if len(suit_vals) >= 5:
                flush_vals = sorted(suit_vals, reverse=True)[:5]
                break

        # Straight: 5 consecutive unique values anywhere in the hand
        unique = sorted(set(values), reverse=True)
        straight_high = 0
        for i in range(len(unique) - 4):
            if unique[i] - unique[i + 4] == 4:
                straight_high = unique[i]
                break
        if not straight_high and {14, 2, 3, 4, 5}.issubset(set(values)):
            straight_high = 5

        # Straight flush: 5 consecutive cards that are ALL the same suit
        sf_high = 0
        for suit_vals in by_suit.values():
            if len(suit_vals) >= 5:
                su = sorted(set(suit_vals), reverse=True)
                for i in range(len(su) - 4):
                    if su[i] - su[i + 4] == 4:
                        sf_high = max(sf_high, su[i])
                        break
                if not sf_high and {14, 2, 3, 4, 5}.issubset(set(suit_vals)):
                    sf_high = 5

        # Return (score_tuple, name) — tuples compare lexicographically for free
        if sf_high:
            return (8, sf_high), "Straight Flush"
        if rc[0] == 4:
            kicker = next(v for v in values if v != rv[0])
            return (7, rv[0], kicker), "Four of a Kind"
        if rc[0] == 3 and len(rc) > 1 and rc[1] >= 2:
            return (6, rv[0], rv[1]), "Full House"
        if flush_vals:
            return (5, *flush_vals), "Flush"
        if straight_high:
            return (4, straight_high), "Straight"
        if rc[0] == 3:
            kickers = [v for v in values if v != rv[0]][:2]
            return (3, rv[0], *kickers), "Three of a Kind"
        if rc[0] == 2 and len(rc) > 1 and rc[1] == 2:
            kicker = next(v for v in values if v not in (rv[0], rv[1]))
            return (2, rv[0], rv[1], kicker), "Two Pair"
        if rc[0] == 2:
            kickers = [v for v in values if v != rv[0]][:3]
            return (1, rv[0], *kickers), "One Pair"
        return (0, *values[:5]), "High Card"

    # ── SETUP ────────────────────────────────────────────────────────────────

    def setup_players(self):
        name = input("  Enter your name, friend: ").strip() or "Stranger"
        self.players = [HmnPlayer(name, chips=1000)]

        used_names = []
        for _ in range(3):
            available = [n for n in self.COMP_NAMES if n not in used_names]
            comp_name = rand_choice(available)
            used_names.append(comp_name)
            self.players.append(CmpPlayer(comp_name, chips=1000))

        print("\n  Players at the table:")
        for p in self.players:
            print(f"    {p.name} — ${p.chips}")

    # ── DEALING ──────────────────────────────────────────────────────────────

    def deal_hole_cards(self):
        """Deal 2 cards to each player."""
        for _ in range(2):
            for player in self.players:
                player.receive_card(self.deck.deal())

    def deal_community_cards(self, count):
        """Deal cards to the shared community board."""
        for _ in range(count):
            self.community_cards.append(self.deck.deal())

    # ── BETTING ROUND ────────────────────────────────────────────────────────

    def betting_round(self, round_name, current_bet=0, player_amounts=None, action_order=None):
        """
        Run one full betting round, going around the table until every active
        player has acted and matched the current bet (or folded).

        current_bet:   the amount everyone must match to stay in (0 = free to check)
        player_amounts: chips each player already put in THIS round (used for blinds)
        action_order:  explicit player order — used pre-flop so BB acts last
        """
        print(f"\n  --- {round_name} ---")
        if self.community_cards:
            print(f"  Board: {' '.join(str(c) for c in self.community_cards)}")
        print(f"  Pot: ${self.pot}")

        # Track how much each player has put in during this betting round only
        amount_in = {p.name: (player_amounts or {}).get(p.name, 0) for p in self.players}

        # Use the provided order if given, otherwise default table order.
        # Pre-flop passes an explicit order so the big blind gets to act last.
        base_order = action_order if action_order is not None else self.players
        action_queue = [p for p in base_order if not p.folded]

        while action_queue:
            still_in = [p for p in self.players if not p.folded]
            if len(still_in) <= 1:
                break

            player = action_queue.pop(0)
            if player.folded:
                continue

            to_call  = max(0, current_bet - amount_in[player.name])
            action   = player.decide_action(self.community_cards, current_bet, to_call)
            raise_by = self.BIG_BLIND
            if isinstance(action, tuple):
                action, raise_by = action

            if action == "fold":
                player.folded = True
                print(f"  {player.name} folds.  ({rand_choice(self.FOLD_QUOTES)})")

            elif action == "check":
                print(f"  {player.name} checks.")

            elif action == "call":
                amount = min(to_call, player.chips)
                player.chips        -= amount
                self.pot            += amount
                amount_in[player.name] += amount
                if amount < to_call:  # all-in, couldn't fully match
                    print(f"  {player.name} calls all-in for ${amount}. Pot: ${self.pot}")
                elif amount < current_bet:  # had chips in already (e.g. SB completing to BB)
                    print(f"  {player.name} calls ${current_bet} (adds ${amount}). Pot: ${self.pot}")
                else:
                    print(f"  {player.name} calls ${current_bet}. Pot: ${self.pot}")

            elif action == "raise":
                new_bet    = current_bet + raise_by
                to_put_in  = min(new_bet - amount_in[player.name], player.chips)
                player.chips           -= to_put_in
                self.pot               += to_put_in
                amount_in[player.name] += to_put_in
                current_bet = amount_in[player.name]
                # Everyone still in (except the raiser) must respond, preserving street order
                action_queue = [p for p in base_order if not p.folded and p is not player]
                print(f"  {player.name} raises to ${current_bet}. Pot: ${self.pot}  I'm your huckleberry.")

    # ── SHOWDOWN ─────────────────────────────────────────────────────────────

    def showdown(self):
        """Evaluate all remaining hands and find the winner."""
        print("\n  ===== SHOWDOWN =====")
        print("  'You tell 'em we're comin'... and hell's comin' with us.' — Wyatt Earp")
        print(f"  Final board: {' '.join(str(c) for c in self.community_cards)}")

        active_players = [p for p in self.players if not p.folded]

        for player in active_players:
            score, name       = self.evaluate_hand(player.hand, self.community_cards)
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

        print("\n" + "="*44)
        print("  NEW HAND")
        print("="*44)

        # Compute seat positions from the dealer button (all indices mod n)
        n   = len(self.players)
        btn = self.btn_idx % n
        sb  = (btn + 1) % n   # small blind: one seat left of button
        bb  = (btn + 2) % n   # big blind:   one seat left of small blind

        # Post blinds
        if n >= 2:
            self.players[sb].chips -= self.SMALL_BLIND
            self.pot               += self.SMALL_BLIND
            self.players[bb].chips -= self.BIG_BLIND
            self.pot               += self.BIG_BLIND
            print(f"  {self.players[sb].name} posts small blind (${self.SMALL_BLIND})")
            print(f"  {self.players[bb].name} posts big blind (${self.BIG_BLIND})")

        # Deal hole cards (2 per player)
        self.deal_hole_cards()

        # Pre-flop action order:
        #   Standard (3+ players): UTG first, then clockwise, SB second-to-last, BB last
        #   Heads-up (2 players):  BTN/SB acts first, BB acts last
        blinds = {
            self.players[sb].name: self.SMALL_BLIND,
            self.players[bb].name: self.BIG_BLIND,
        }
        if n == 2:
            preflop_order = [self.players[btn], self.players[bb]]
        else:
            utg = (bb + 1) % n
            preflop_order = [self.players[(utg + i) % n] for i in range(n)]

        self.betting_round("Pre-Flop", current_bet=self.BIG_BLIND,
                           player_amounts=blinds, action_order=preflop_order)

        # Post-flop action order:
        #   Standard (3+ players): SB first, clockwise, BTN last
        #   Heads-up (2 players):  BB first, BTN/SB last
        if n == 2:
            postflop_order = [self.players[bb], self.players[btn]]
        else:
            postflop_order = [self.players[(sb + i) % n] for i in range(n)]

        active = [p for p in self.players if not p.folded]
        if len(active) == 0:
            print("\n  Everyone folded — hand cancelled.")
            return
        if len(active) == 1:
            winner = active[0]
        else:
            # Flop — 3 community cards face up
            self.deal_community_cards(3)
            self.betting_round("Flop", action_order=postflop_order)
            active = [p for p in self.players if not p.folded]

            if len(active) == 0:
                print("\n  Everyone folded — hand cancelled.")
                return
            if len(active) == 1:
                winner = active[0]
            else:
                # Turn — 1 more card
                self.deal_community_cards(1)
                self.betting_round("Turn", action_order=postflop_order)
                active = [p for p in self.players if not p.folded]

                if len(active) == 0:
                    print("\n  Everyone folded — hand cancelled.")
                    return
                if len(active) == 1:
                    winner = active[0]
                else:
                    # River — final card
                    self.deal_community_cards(1)
                    self.betting_round("River", action_order=postflop_order)
                    active = [p for p in self.players if not p.folded]

                    if len(active) == 0:
                        print("\n  Everyone folded — hand cancelled.")
                        return
                    if len(active) == 1:
                        winner = active[0]
                    else:
                        winner = self.showdown()

        # Award the pot to the winner
        winner.chips += self.pot
        print(f"\n  *** {winner.name} wins the pot of ${self.pot}! ***")
        print(f"  'You're no daisy at all.' — Doc Holliday")
        if winner.hand_name:
            print(f"      (Winning hand: {winner.hand_name})")

    # ── GAME SESSION ──────────────────────────────────────────────────────────

    def play_game(self):
        """Full game session — play hands until someone is broke or player quits."""
        print("")
        print("  ╔══════════════════════════════════════════╗")
        print("  ║        TOMBSTONE TEXAS HOLD'EM           ║")
        print("  ║                                          ║")
        print("  ║   'I have not yet begun to defile        ║")
        print("  ║    myself.' — Doc Holliday               ║")
        print("  ╚══════════════════════════════════════════╝")

        # Resume a saved game if one exists, otherwise run normal setup
        if os.path.exists(self.SAVE_FILE):
            ans = input("\n  Found a saved game — resume it? (y/n): ").strip().lower()
            if ans in ["y", "yes"]:
                self.load_game()
                print("\n  Picking up where you left off:")
                for p in self.players:
                    print(f"    {p.name}: ${p.chips}")
            else:
                self.setup_players()
        else:
            self.setup_players()

        game_on = True
        while game_on:
            self.play_hand()

            # Remove any player who ran out of chips
            broke_players = [p for p in self.players if p.chips <= 0]
            for p in broke_players:
                print(f"\n  {p.name} is cleaned out.")
                print(f"  'It appears the strain was more than he could bear.'")
            self.players = [p for p in self.players if p.chips > 0]

            if len(self.players) == 1:
                print(f"\n  Game over! {self.players[0].name} wins everything!")
                print(f"  'Hell's comin' with me!' — Wyatt Earp")
                game_on = False
                break

            # Advance the dealer button one seat clockwise
            self.btn_idx = (self.btn_idx + 1) % len(self.players)

            # Show chip counts
            print("\n  Chip counts:")
            for p in self.players:
                print(f"    {p.name}: ${p.chips}")

            while True:
                again = input("\n  Play another hand? (y / n / s to save): ").strip().lower()
                if again in ["y", "yes"]:
                    break
                elif again in ["n", "no"]:
                    game_on = False
                    break
                elif again in ["s", "save"]:
                    self.save_game()
                    game_on = False
                    break
                # anything else: re-ask, don't quit

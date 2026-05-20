# ── TEXAS HOLD'EM MANAGER ───────────────────────────────────────────────────
# Controls the entire game: setup, blinds, dealing, betting rounds, showdown.
# One instance manages multiple hands in a session.

from deck import Deck
from players import PokerPlayer, HumanPokerPlayer, ComputerPokerPlayer
from hand_evaluator import HandEvaluator
from random import randint, choice as rand_choice


class TexasHoldemManager:

    COMP_NAMES = [
        "Angela", "Brett", "Carlos", "Diana", "Eddie", "Fiona",
        "Hector", "Iris", "Jake", "Karen", "Leo", "Monica"
    ]

    SMALL_BLIND = 25
    BIG_BLIND   = 50

    def __init__(self):
        self.deck            = Deck()
        self.players         = []
        self.community_cards = []
        self.pot             = 0
        self.current_bet     = 0
        self.btn_idx         = 0

    # ── SETUP ────────────────────────────────────────────────────────────────

    def setup_game(self):
        """Ask for player name, build 3 computer opponents."""
        print("\n" + "="*50)
        print("         TEXAS HOLD'EM POKER")
        print("="*50)
        name = input("\nEnter your name: ").strip() or "Player"
        self.players = [HumanPokerPlayer(name, chips=1000)]

        available_names = self.COMP_NAMES[:]
        for _ in range(3):
            comp_name = rand_choice(available_names)
            available_names.remove(comp_name)
            self.players.append(ComputerPokerPlayer(comp_name, chips=1000))

        print(f"\nPlayers at the table:")
        for p in self.players:
            print(f"  {p.name}  —  ${p.chips}")

    # ── ROUND SETUP ─────────────────────────────────────────────────────────

    def reset_round(self):
        """Prepare for a new hand: fresh deck, clear all player hands."""
        self.community_cards = []
        self.pot             = 0
        self.current_bet     = 0
        self.deck.reset()
        for player in self.players:
            player.clear_for_new_hand()

    def _collect_blinds(self):
        """Rotate blinds based on round count. Small blind = index 1, big = index 2."""
        n = len(self.players)
        sb_player = self.players[1 % n]
        bb_player = self.players[2 % n]

        sb_amount = min(self.SMALL_BLIND, sb_player.chips)
        bb_amount = min(self.BIG_BLIND,   bb_player.chips)

        sb_player.chips      -= sb_amount
        sb_player.current_bet = sb_amount
        bb_player.chips      -= bb_amount
        bb_player.current_bet = bb_amount

        self.pot          = sb_amount + bb_amount
        self.current_bet  = bb_amount

        print(f"\n  {sb_player.name} posts small blind  (${sb_amount})")
        print(f"  {bb_player.name} posts big blind    (${bb_amount})")

    def _deal_hole_cards(self):
        """Give each player 2 cards, one at a time (proper dealing order)."""
        for _ in range(2):
            for player in self.players:
                player.receive_card(self.deck.deal())

    def _deal_community(self, count):
        """Burn a card (skip it) then deal 'count' community cards face-up."""
        self.deck.deal()    # Burn card — standard poker practice
        for _ in range(count):
            self.community_cards.append(self.deck.deal())

    def _show_community(self, label="Community"):
        if not self.community_cards:
            return
        cards_str = "  ".join(str(c) for c in self.community_cards)
        print(f"\n  {label}: {cards_str}")

    # ── BETTING ──────────────────────────────────────────────────────────────

    def _betting_round(self, round_name, current_bet=0, player_amounts=None, action_order=None):
        """
        Run one betting round using an action queue.
        After a raise, everyone else gets another turn at the new bet level.
        action_order controls initial seat order; rebuilds after raises use self.players.
        """
        print(f"\n{'─'*50}")
        print(f"  {round_name.upper()}")
        print(f"{'─'*50}")
        self._show_community()

        # Track how much each player put in this round; seed with blind credits if given
        amount_in = {p.name: 0 for p in self.players}
        if player_amounts:
            for name, amt in player_amounts.items():
                if name in amount_in:
                    amount_in[name] = amt

        active = [p for p in self.players if not p.folded and p.chips > 0]
        if len(active) <= 1:
            return

        # Use caller-supplied order for the initial queue; rebuild uses self.players after a raise
        action_queue = [p for p in (action_order or self.players)
                        if not p.folded and p.chips > 0]

        while action_queue:
            player = action_queue.pop(0)
            if player.folded or player.chips <= 0:
                continue

            to_call = max(0, current_bet - amount_in[player.name])
            action  = player.decide_action(self.community_cards, current_bet, to_call, self.BIG_BLIND)

            # Human raise returns ("raise", amount); AI raise returns the string "raise"
            action_str = action[0] if isinstance(action, tuple) else action
            raise_by   = action[1] if isinstance(action, tuple) else self.BIG_BLIND

            if action_str == "fold":
                player.folded = True
                print(f"  {player.name} folds.")

            elif action_str in ("call", "check"):
                amount = min(to_call, player.chips)
                player.chips           -= amount
                amount_in[player.name] += amount
                player.current_bet     += amount
                self.pot               += amount
                if to_call == 0:
                    print(f"  {player.name} checks.")
                elif amount < to_call:
                    print(f"  {player.name} calls all-in ${amount_in[player.name]}. Pot: ${self.pot}")
                elif amount < current_bet:
                    print(f"  {player.name} calls ${current_bet} (adds ${amount}). Pot: ${self.pot}")
                else:
                    print(f"  {player.name} calls ${current_bet}. Pot: ${self.pot}")

            elif action_str == "raise":
                new_bet  = current_bet + raise_by
                total    = new_bet - amount_in[player.name]
                amount   = min(total, player.chips)
                player.chips           -= amount
                amount_in[player.name] += amount
                player.current_bet     += amount
                current_bet             = amount_in[player.name]
                self.current_bet        = current_bet
                self.pot               += amount
                print(f"  {player.name} raises to ${current_bet}. Pot: ${self.pot}.")

                # Raise — everyone else gets another turn at the new bet level
                action_queue = [p for p in self.players
                                if not p.folded and p.chips > 0 and p is not player]

            if len([p for p in self.players if not p.folded]) <= 1:
                break

        print(f"\n  Pot after {round_name}: ${self.pot}")

    # ── SHOWDOWN & WINNER ────────────────────────────────────────────────────

    def _evaluate_all_hands(self):
        """Score every player still in the hand."""
        for player in self.players:
            if not player.folded:
                score, name, _ = HandEvaluator.best_hand(player.hand, self.community_cards)
                player.best_hand_score = score
                player.best_hand_name  = name

    def _showdown(self):
        """Reveal all active players' hands and best hand names."""
        print(f"\n{'='*50}")
        print("  SHOWDOWN")
        print(f"{'='*50}")
        self._show_community("Board")
        print()
        for player in self.players:
            if not player.folded:
                player.show_hand()

    def _determine_winner(self):
        """Return the player with the highest hand score."""
        active = [p for p in self.players if not p.folded]
        if not active:
            return self.players[0]
        return max(active, key=lambda p: p.best_hand_score)

    # ── HAND FLOW ────────────────────────────────────────────────────────────

    def play_hand(self):
        """Run one complete hand of Texas Hold'em."""
        self.reset_round()

        print(f"\n{'='*50}")
        print("  NEW HAND")
        print(f"{'='*50}")

        # Compute seat positions from btn_idx
        n   = len(self.players)
        btn = self.btn_idx % n
        sb  = (btn + 1) % n
        bb  = (btn + 2) % n

        sb_player = self.players[sb]
        bb_player = self.players[bb]
        sb_amount = min(self.SMALL_BLIND, sb_player.chips)
        bb_amount = min(self.BIG_BLIND,   bb_player.chips)
        sb_player.chips -= sb_amount
        bb_player.chips -= bb_amount
        self.pot = sb_amount + bb_amount

        print(f"\n  {sb_player.name} posts small blind  (${sb_amount})")
        print(f"  {bb_player.name} posts big blind    (${bb_amount})")

        self._deal_hole_cards()

        # Show the human their hole cards
        human = next((p for p in self.players if isinstance(p, HumanPokerPlayer)), None)
        if human:
            print(f"\n  Your hole cards:")
            for card in human.hand:
                print(f"    {card}")

        # Pre-flop order: UTG first, BB acts last
        if n == 2:
            preflop_order = [self.players[btn], self.players[bb]]
        else:
            utg = (bb + 1) % n
            preflop_order = [self.players[(utg + i) % n] for i in range(n)]

        # Post-flop order: SB first, BTN acts last
        if n == 2:
            postflop_order = [self.players[bb], self.players[btn]]
        else:
            postflop_order = [self.players[(sb + i) % n] for i in range(n)]

        blinds = {sb_player.name: sb_amount, bb_player.name: bb_amount}

        # ── Pre-Flop ─────────────────────────────────────────────────────────
        self._betting_round("Pre-Flop", current_bet=bb_amount,
                            player_amounts=blinds, action_order=preflop_order)

        active = [p for p in self.players if not p.folded]
        if len(active) == 1:
            return self._award_pot(active[0])

        # ── Flop (3 community cards) ─────────────────────────────────────────
        self._deal_community(3)
        self._betting_round("Flop", action_order=postflop_order)

        active = [p for p in self.players if not p.folded]
        if len(active) == 1:
            return self._award_pot(active[0])

        # ── Turn (1 more community card) ─────────────────────────────────────
        self._deal_community(1)
        self._betting_round("Turn", action_order=postflop_order)

        active = [p for p in self.players if not p.folded]
        if len(active) == 1:
            return self._award_pot(active[0])

        # ── River (final community card) ─────────────────────────────────────
        self._deal_community(1)
        self._betting_round("River", action_order=postflop_order)

        active = [p for p in self.players if not p.folded]
        if len(active) == 1:
            return self._award_pot(active[0])

        # ── Showdown ─────────────────────────────────────────────────────────
        self._evaluate_all_hands()
        self._showdown()
        winner = self._determine_winner()
        return self._award_pot(winner)

    def _award_pot(self, winner):
        """Give the pot to the winner and print the result."""
        winner.chips += self.pot
        print(f"\n  *** {winner.name} wins ${self.pot}! ***")
        if winner.best_hand_name:
            print(f"      ({winner.best_hand_name})")
        return winner

    # ── FULL GAME SESSION ────────────────────────────────────────────────────

    def play_game(self):
        """Loop through hands until someone is out of chips or player quits."""
        self.setup_game()

        while True:
            self.play_hand()

            # Remove broke players
            self.players = [p for p in self.players if p.chips > 0]

            # Game over if only one player left
            if len(self.players) == 1:
                print(f"\n  {self.players[0].name} wins the game with ${self.players[0].chips}!")
                break

            # Chip counts
            print(f"\n  Chip counts:")
            for p in self.players:
                print(f"    {p.name}: ${p.chips}")

            again = input("\n  Play another hand? (y/n): ").strip().lower()
            if again not in ["y", "yes"]:
                print("\n  Thanks for playing!")
                break

            # Advance the button index so blinds rotate each hand
            self.btn_idx = (self.btn_idx + 1) % len(self.players)

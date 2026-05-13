# ── HAND EVALUATOR ──────────────────────────────────────────────────────────
# Given 7 cards (2 hole + 5 community), finds the best possible 5-card hand.
# Returns a (score_tuple, hand_name, best_five_cards) so hands can be compared.
#
# Score tuples compare like this: higher first element = better hand type.
# Within the same hand type, later elements break ties.
# Python compares tuples element-by-element left-to-right — exactly what we need.
#
# Hand ranks:
#   8 = Straight Flush (Ace-high = Royal Flush, named separately)
#   7 = Four of a Kind
#   6 = Full House
#   5 = Flush
#   4 = Straight
#   3 = Three of a Kind
#   2 = Two Pair
#   1 = One Pair
#   0 = High Card

from itertools import combinations
from collections import Counter


class HandEvaluator:

    @staticmethod
    def best_hand(hole_cards, community_cards):
        """
        Try all 21 possible 5-card combinations from 7 cards.
        Return the best: (score_tuple, hand_name, [best 5 cards])
        """
        all_cards = hole_cards + community_cards
        best_score = None
        best_name = "High Card"
        best_five = []

        for five in combinations(all_cards, 5):
            score, name = HandEvaluator._score_five(list(five))
            if best_score is None or score > best_score:
                best_score = score
                best_name = name
                best_five = list(five)

        return best_score, best_name, best_five

    @staticmethod
    def _score_five(cards):
        """
        Score a 5-card hand. Returns (comparable_tuple, hand_name_string).
        """
        values = sorted([c.value for c in cards], reverse=True)
        suits  = [c.suit for c in cards]
        counts = Counter(values)

        is_flush = (len(set(suits)) == 1)

        # Straight detection
        is_straight = False
        straight_high = 0
        unique_vals = sorted(set(values), reverse=True)

        if len(unique_vals) == 5:
            if unique_vals[0] - unique_vals[4] == 4:
                is_straight = True
                straight_high = unique_vals[0]
            elif set(unique_vals) == {14, 2, 3, 4, 5}:
                # Wheel: A-2-3-4-5 — Ace plays LOW here
                is_straight = True
                straight_high = 5

        # Sort by (count desc, value desc) to get pairs/trips/quads first
        ranked_pairs = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
        sorted_vals   = [v for v, _ in ranked_pairs]

        # ── HAND TYPE CHECKS ────────────────────────────────────────────────

        if is_straight and is_flush:
            name = "Royal Flush" if straight_high == 14 else "Straight Flush"
            return (8, straight_high), name

        if sorted_vals and counts[sorted_vals[0]] == 4:
            kicker = sorted_vals[1]
            return (7, sorted_vals[0], kicker), "Four of a Kind"

        cnt_list = [counts[v] for v in sorted_vals]
        if len(cnt_list) >= 2 and cnt_list[0] == 3 and cnt_list[1] == 2:
            return (6, sorted_vals[0], sorted_vals[1]), "Full House"

        if is_flush:
            return (5,) + tuple(values), "Flush"

        if is_straight:
            return (4, straight_high), "Straight"

        if cnt_list and cnt_list[0] == 3:
            kickers = sorted([v for v, c in counts.items() if c == 1], reverse=True)
            return (3, sorted_vals[0]) + tuple(kickers), "Three of a Kind"

        if len(cnt_list) >= 2 and cnt_list[0] == 2 and cnt_list[1] == 2:
            pair_vals = sorted([v for v, c in counts.items() if c == 2], reverse=True)
            kicker    = max(v for v, c in counts.items() if c == 1)
            return (2, pair_vals[0], pair_vals[1], kicker), "Two Pair"

        if cnt_list and cnt_list[0] == 2:
            pair_val = max(v for v, c in counts.items() if c == 2)
            kickers  = sorted([v for v, c in counts.items() if c == 1], reverse=True)
            return (1, pair_val) + tuple(kickers), "One Pair"

        # High card — all 5 values for complete tie-breaking
        return (0,) + tuple(values), "High Card"

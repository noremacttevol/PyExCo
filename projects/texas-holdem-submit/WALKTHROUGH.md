# Texas Hold'em — How I Built This (Cameron's Learning Notes)

> This document is my own notes on how the project came together.
> If Daniel asks me to explain something, this is what I'd say.

---

## Why Texas Hold'em?

Daniel said the blackjack app he built was designed to be expandable to other card games.
He literally said "later on you could write in a poker game or something if you want."
Texas Hold'em uses a standard 52-card deck, has players, and needs a game manager — same structure as blackjack, just with different rules.

---

## The File Structure (Why 5 Files?)

Same reason Daniel split blackjack into multiple files — **modularity**.

Think of it like a panel wiring as-built vs a single-line diagram. The single-line shows you the big picture. The as-built has every single wire, terminal, and tag. You need both. Splitting into files means if you want to change how cards work, you only touch `card.py`. You don't have to dig through 500 lines of game logic.

```
card.py           → One card. Rank, suit, value.
deck.py           → 52 cards. Shuffle. Deal one at a time.
players.py        → Base player class + human player class (inheritance)
holdem_manager.py → The whole game: deal, bet, evaluate, find winner
main.py           → The menu. Just calls holdem_manager.
```

---

## card.py — What I Learned

A class is a blueprint. `Card` is the blueprint for every card in the deck.

The `RANK_VALUES` dictionary at the top is a **class-level constant** — it belongs to the Card class itself, not to any one card. Every card can look it up.

`__init__` runs automatically when you create a card: `Card("Ace", "Spades")`
- `self` = this specific card being created
- `self.rank` = stores the rank ON this card permanently
- `self.value` = looks up the number from the dictionary

`__repr__` controls what prints when you do `print(card)` — without it you'd get something like `<Card object at 0x7f3c...>` which is useless.

**What I'd say to Daniel:** "I built the Card class the same way you built yours for blackjack — rank, suit, and a value lookup from a dictionary. The `__repr__` method makes it readable when printed."

---

## deck.py — What I Learned

The Deck builds all 52 cards using two nested for loops — one for suits, one for ranks.
That's 4 suits × 13 ranks = 52 cards. `shuffle()` from the `random` module randomizes them.

`deal()` uses `.pop()` to remove and return the last card — same as what Daniel used.

`reset()` rebuilds the whole deck — needed at the start of every new hand so we're not dealing from a depleted deck.

**What I'd say to Daniel:** "Deck is nearly identical to your version. I import `Card` from card.py and build all 52 by looping through suits and ranks. `reset()` rebuilds it fresh for each hand."

---

## players.py — What I Learned (The OOP Part)

This is where inheritance and polymorphism show up — the core Python 2 concepts.

**`PokerPlayer`** (base class / parent / computer player):
- Has all the attributes: `hand`, `chips`, `folded`, `score`
- Has `decide_action()` — computer logic: if pocket pair + high card, raise. If weak, fold.
- Has `show_hand()` — prints cards and hand name

**`HumanPokerPlayer`** (child class / subclass):
- Inherits EVERYTHING from `PokerPlayer` — `hand`, `chips`, `receive_card()`, `clear_hand()`, all of it
- Only overrides `decide_action()` — instead of auto-deciding, it asks the player to type

This is polymorphism: the game manager calls `player.decide_action()` on every player in the list. For computer players it runs the auto logic. For the human player it runs the input prompt. Same function call, different behavior. The game manager doesn't need to know which type it's dealing with.

**What I'd say to Daniel:** "Same pattern you used for BlackJackPlayer and HumBlackJackPlayer. Base class handles the computer behavior. The human subclass only overrides `decide_action` to take keyboard input instead of auto-deciding. The game manager loops through all players and calls `decide_action` without caring what type they are — that's the polymorphism."

---

## holdem_manager.py — What I Learned

This is the brain. It knows:
- How to set up players
- How to deal cards (hole cards + community cards)
- How to run betting rounds
- How to evaluate hands
- How to find the winner

### Hand Evaluation

This was the hardest part to figure out.

Texas Hold'em: each player has 2 hole cards + there are 5 community cards = 7 cards total.
You need to find the best possible hand from those 7 cards.

My approach: evaluate all 7 cards together and look for each hand type:

```
1. Count how many of each value we have (using a dictionary)
2. Count how many of each suit we have
3. Check if 5 cards are in a row (straight)
4. Then check from best hand to worst and return the first match
```

```python
# Count values using a dictionary
value_counts = {}
for v in values:
    value_counts[v] = value_counts.get(v, 0) + 1

counts = sorted(value_counts.values(), reverse=True)
# If counts[0] == 4 → four of a kind
# If counts[0] == 3 → three of a kind (or full house if counts[1] == 2)
# etc.
```

Hand ranks (score numbers I assigned):
```
8 = Straight Flush
7 = Four of a Kind
6 = Full House
5 = Flush
4 = Straight
3 = Three of a Kind
2 = Two Pair
1 = One Pair
0 = High Card
```

Higher score wins. That's it.

### Betting Round

Each player calls `decide_action()`. Based on what comes back:
- `"fold"` → mark them as folded, skip them from now on
- `"call"` → subtract chips, add to pot
- `"raise"` → subtract more chips, add more to pot

If everyone folds except one person, that person wins without a showdown.

### The Hand Flow

```
deal hole cards
  → pre-flop betting
    → deal flop (3 community cards)
      → flop betting
        → deal turn (1 card)
          → turn betting
            → deal river (1 card)
              → river betting
                → showdown → find winner
```

At each step, if only 1 player is left (everyone else folded), they win immediately.

**What I'd say to Daniel:** "The manager handles the full hand flow — blinds, 4 betting rounds, and showdown. The hand evaluator works by counting value and suit occurrences and checking for each hand type from best to worst. I assign a score number to each hand type and the highest score wins."

---

## main.py — What I Learned

Daniel's 3-section pattern:
1. Imports at top
2. `def main()` with all the logic inside
3. `main()` called at the bottom (I used `if __name__ == "__main__"` which Daniel mentioned is the professional version)

The menu loops with `while app_on` — when the user picks quit, `app_on` goes `False` and the loop ends. Boolean flag pattern from Day 5.

---

## Concepts From Class I Used In This Project

| Concept | Where It Shows Up | Course Day |
|---------|-------------------|------------|
| Classes & Objects | Card, Deck, PokerPlayer, TexasHoldemManager | Py2 Day 1-2 |
| `__init__`, `self` | Every class | Py2 Day 2 |
| `__repr__` | Card class | Py2 Day 3 |
| Inheritance | HumanPokerPlayer extends PokerPlayer | Py2 Day 3-4 |
| Polymorphism | `decide_action()` on different player types | Py2 Day 1 |
| Multi-file structure | 5 files, each one class | Py2 Day 2 |
| Dictionaries | RANK_VALUES, value_counts, suit_counts | Py1 Day 5 |
| Lists | hand, cards, players, community_cards | Py1 Day 5 |
| For loops | Building deck, dealing, betting rounds | Py1 Day 5 |
| While loops | Game loop, hand loop | Py1 Day 5 |
| Imports | card → deck, players → manager → main | Py1 Day 4 |
| Boolean flags | `app_on`, `game_on`, `folded` | Py1 Day 5-6 |
| f-strings | All print statements | Py1 Day 3 |
| `if __name__ == "__main__"` | main.py | Py2 (mentioned) |

---

## What Daniel Might Ask and What to Say

**Q: "Walk me through the Card class."**
> "Card has three attributes: rank (like 'Ace'), suit (like 'Spades'), and value. Value is looked up from a class dictionary called RANK_VALUES that maps rank names to numbers. That lets me compare cards mathematically. `__init__` sets those three attributes when you create a card. `__repr__` makes it print readable."

**Q: "How does inheritance work in your players?"**
> "PokerPlayer is the base class — it has all the attributes and the computer logic for deciding actions. HumanPokerPlayer is a subclass — it inherits everything but overrides just the `decide_action` method. So instead of the computer deciding, it asks the player to type. The game manager can call `decide_action()` on any player in the list without checking what type it is."

**Q: "How does hand evaluation work?"**
> "I count how many of each card value appears, and how many of each suit. Then I check for hand types from best to worst — straight flush, four of a kind, full house, and so on. I assign each hand type a score number, and the player with the highest score wins."

**Q: "Why multiple files?"**
> "Same reason you split blackjack into separate files — if I want to change how the Deck works, I only touch deck.py. The other files don't need to change. It also makes it easier to find things when the project gets bigger."

**Q: "Did you write this yourself?"**
> "I designed the architecture and the game logic. I use AI to help me with syntax because I'm still learning it — you've seen me do that. I understand what every piece does and why."

---

## Known Limitations (What I'd Fix With More Time)

- Hand comparison on ties isn't perfect — if two players both have "Two Pair", it compares the score number (both are 2) and just picks whoever is first in the list. A full version would compare the actual pair values.
- No side pots — if someone goes all-in with fewer chips, it should only win what they put in from each player.
- Betting amounts are fixed (just big blind × 1 or × 2). A full version would let you raise to any amount.
- No blind rotation — in real poker, blinds move clockwise every hand. I rotate the player list, which approximates this.

# LEARN IT — How This Game Actually Works
### (Written like I'm explaining it to someone who has never seen Python)

> Read this top to bottom. Zero Python knowledge assumed.
> If Daniel asks me to walk through my code, this is what I rehearsed.

---

## The Big Picture First

I built a Texas Hold'em poker game that runs in the terminal.
It has 5 files. Each file handles exactly one job:

| File | Its One Job |
|------|-------------|
| `card.py` | Knows what one playing card is |
| `deck.py` | Knows how to build and shuffle 52 cards |
| `players.py` | Knows what a player looks like (computer or human) |
| `manager.py` | Actually runs the game — deals, bets, finds winner |
| `main.py` | The front door — shows the menu, starts things up |

They talk to each other in a chain:
```
main.py → manager.py → players.py
                     → deck.py → card.py
```

When you run `python main.py`, that chain fires in order and loads everything.

---

## Before Any Code: What Even Is a .py File?

A `.py` file is just a text file. Python reads it like a recipe — top to bottom, one line at a time.

When a file says `from deck import Deck` at the top, it means:
> "Go find the file called `deck.py` and grab the thing named `Deck` out of it."

That's how all 5 files talk to each other.

---

## The Most Important Thing: What Is a Class?

A **class** is a blueprint for making things.

The `Card` class is the blueprint for one playing card.
The `Deck` class is the blueprint for a full deck.
The `CmpPlayer` class is the blueprint for a player.

When you USE the blueprint to make one actual thing, that thing is called an **object**
(also called an **instance**).

```python
my_card = Card("Ace", "Spades")
```

That line makes ONE actual card using the Card blueprint.
`my_card` is the object. `Card` is the blueprint.

You can make as many cards as you want from the same blueprint. Each one is its own object
with its own data.

---

## What Is `self`?

`self` means "this specific object."

If you have three different cards, each one is a different object.
When a card says `self.rank`, it means "MY rank, stored on ME."

```python
card1 = Card("Ace", "Spades")    # self.rank = "Ace" for THIS card
card2 = Card("King", "Hearts")   # self.rank = "King" for THIS card
```

`self` is just Python's way of saying "this one, specifically."
You'll see it everywhere. It's not magic.

---

## What Is `__init__`?

`__init__` is the setup function. It runs automatically the moment you create an object.

```python
my_card = Card("Ace", "Spades")
```

The instant that line runs, Python calls `__init__` automatically and sets up the card.
You don't call `__init__` yourself — Python does it for you.

Inside `__init__`, `self` refers to the new card being created right now.

---

## FILE 1: card.py — The Playing Card Blueprint

```python
class Card:
```
This line declares the blueprint. Everything indented underneath it belongs to the Card class.

```python
    RANK_VALUES = {
        "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
        "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
        "Jack": 11, "Queen": 12, "King": 13, "Ace": 14
    }
```
This is a **class-level dictionary**. It belongs to the Card class itself, not to any one card.
Every card can look up a number from it. `"Ace"` maps to `14`. `"King"` maps to `13`.
This lets us do math on cards — higher number wins.

```python
    def __init__(self, rank="Two", suit="Clubs"):
        self.rank  = rank
        self.suit  = suit
        self.value = self.RANK_VALUES[rank]
```
This runs when you do `Card("Ace", "Spades")`.
- `self.rank = "Ace"` — this card remembers its rank
- `self.suit = "Spades"` — this card remembers its suit
- `self.value = 14` — looks up "Ace" in the dictionary, gets the number 14

Now this card permanently has all three stored on it.

```python
    def __repr__(self):
        return f"[{self.rank} of {self.suit}]"
```
`__repr__` controls what you see when you print a card.

Without it: `<Card object at 0x7f3c...>` — useless garbage.
With it: `[Ace of Spades]` — actually readable.

Python calls `__repr__` automatically whenever it needs to display the object.

```python
    def __str__(self):
        return self.__repr__()
```
`__str__` is used when Python converts a card to a string inside an f-string like `f"{card}"`.
It just calls `__repr__` — same result, two different ways Python asks for it.

---

## FILE 2: deck.py — The 52-Card Deck

```python
from card import Card
from random import shuffle
```
First two lines are imports. `Card` comes from `card.py`. `shuffle` comes from Python's
built-in `random` library (already installed, no download needed).

```python
class Deck:
    RANKS = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
             "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    SUITS = ["Clubs", "Diamonds", "Spades", "Hearts"]
```
Two class-level lists. These never change — every deck has the same 13 ranks and 4 suits.

```python
    def __init__(self):
        self.cards = []
        self.reset()
```
When a Deck is created, `cards` starts as an empty list, then `reset()` fills it.

```python
    def reset(self):
        self.cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(Card(rank, suit))
        shuffle(self.cards)
```
This builds all 52 cards using **nested for loops** — a loop inside a loop:
- Outer loop: goes through each of the 4 suits (Clubs, Diamonds, Spades, Hearts)
- Inner loop: for each suit, goes through all 13 ranks (Two through Ace)
- 4 suits × 13 ranks = 52 cards total

`shuffle(self.cards)` randomizes the order. Done.

`reset()` is also called at the start of each new hand — you can't deal from a depleted deck.

```python
    def deal(self):
        return self.cards.pop()
```
`.pop()` removes and returns the LAST card in the list.
So dealing removes one card from the deck and hands it over.
Daniel used `.pop()` in the List Manager — same concept, different context.

---

## FILE 3: players.py — The Player Blueprints

This is where the Python 2 material shows up: **inheritance** and **polymorphism**.

### CmpPlayer — The Base Class (Computer Player)

```python
class CmpPlayer:
    def __init__(self, name, chips=1000):
        self.name      = name
        self.chips     = chips
        self.hand      = []
        self.folded    = False
        self.score     = 0
        self.hand_name = ""
```
Every player — computer or human — has:
- A name (string)
- Chips (their money, starts at 1000)
- A hand (empty list that cards get added to during the hand)
- `folded` — a boolean flag, True if they've folded and are out of this hand
- `score` and `hand_name` — filled in during hand evaluation at showdown

```python
    def decide_action(self, community_cards):
        v1       = self.hand[0].value
        v2       = self.hand[1].value
        is_pair  = (v1 == v2)
        high_card = max(v1, v2)

        if is_pair and high_card >= 10:
            return "raise"
        if is_pair or high_card >= 12:
            return "call"
        return "fold"
```
This is the computer's decision logic. Simple strategy:
- Pocket pair (both cards same value) AND at least a Ten? Raise.
- Pocket pair OR one Queen/King/Ace? Call.
- Anything else? Fold.

It returns a string. The game manager reads that string and takes the action.

### HmnPlayer — The Child Class (Human Player)

```python
class HmnPlayer(CmpPlayer):
```
The `(CmpPlayer)` in parentheses means: **HmnPlayer inherits from CmpPlayer.**

Inheritance means HmnPlayer gets ALL of CmpPlayer's stuff for free:
- `__init__` (same setup)
- `receive_card`, `clear_hand`, `show_hand` (same methods)
- `__repr__` (same display)

It only CHANGES one thing:

```python
    def decide_action(self, community_cards):
        self.show_hand()
        choice = input("\n  Your action (fold / call / raise): ").lower().strip()
        if choice in ["fold", "f"]:
            return "fold"
        elif choice in ["call", "c", "check"]:
            return "call"
        elif choice in ["raise", "r", "bet", "b"]:
            return "raise"
```
Same function name. But now instead of auto-deciding, it shows your cards and asks you to type.

**This is polymorphism.** The game manager calls `player.decide_action()` on every player
in the list. For computer players, it runs the auto logic. For the human player, it prompts
for input. Same call. Different behavior. The manager never has to check what type it is.

---

## FILE 4: manager.py — The Brain

Biggest file. Runs the entire game. Let me break it into pieces.

### `evaluate_hand()` — Figuring Out Who Has the Best Cards

```python
def evaluate_hand(self, hole_cards, community_cards):
    all_cards = hole_cards + community_cards
    values    = sorted([c.value for c in all_cards], reverse=True)
```
`hole_cards` = your 2 private cards.
`community_cards` = the 5 shared cards on the table.
Together = 7 cards total to work with.

`[c.value for c in all_cards]` is a **list comprehension**.
It's shorthand for this:
```python
values = []
for c in all_cards:
    values.append(c.value)
```
Same result, one line. Daniel mentioned this style — it's just a compact loop.

```python
    value_counts = {}
    for v in values:
        value_counts[v] = value_counts.get(v, 0) + 1

    counts = sorted(value_counts.values(), reverse=True)
```
This counts how many of each value we have using a dictionary.
`.get(v, 0)` means "look up v, and if it's not there yet, use 0 as the default."

Example: if we have two Aces and three Kings:
```
value_counts = {14: 2, 13: 3}
counts = [3, 2]  # sorted biggest first
```

Then checking `counts[0] == 3 and counts[1] == 2` means Full House.

Hand scores assigned (higher = better):
```
8 = Straight Flush   (rarest, best)
7 = Four of a Kind
6 = Full House
5 = Flush
4 = Straight
3 = Three of a Kind
2 = Two Pair
1 = One Pair
0 = High Card        (weakest)
```

The function returns TWO things: `return 6, "Full House"`.
Python can return multiple values separated by a comma — they come back as a pair.

### `betting_round()` — One Round of Betting

```python
for player in self.players:
    if player.folded:
        continue
    action = player.decide_action(self.community_cards)
    if action == "fold":
        player.folded = True
    elif action == "call":
        player.chips -= self.BIG_BLIND
        self.pot     += self.BIG_BLIND
```
Loop through every player. If they already folded, `continue` skips them and moves on.
Otherwise: call `decide_action()`, read the string it returns, and do the action.
`-=` subtracts chips. `+=` adds to the pot.

### `play_hand()` — One Complete Hand

The full sequence of a Texas Hold'em hand:
```
1. Reset: clear cards, reset pot, rebuild and shuffle deck
2. Post blinds (forced bets from 2 players to seed the pot)
3. Deal 2 hole cards to each player
4. Pre-Flop betting round
5. Deal 3 community cards (The Flop)
6. Flop betting round
7. Deal 1 more community card (The Turn)
8. Turn betting round
9. Deal 1 final community card (The River)
10. River betting round
11. Showdown — evaluate hands, find highest score, that player wins
12. Award the pot to the winner
```

At each step after a betting round:
```python
active = [p for p in self.players if not p.folded]
if len(active) == 1:
    winner = active[0]
```
If only 1 player is left standing (everyone else folded), they win immediately.
No need to go to showdown. The hand is over.

### `play_game()` — The Full Session

Loops `play_hand()` over and over until someone's out of chips or the player quits.
After each hand, removes broke players and shows chip counts.

---

## FILE 5: main.py — The Front Door

```python
from manager import TexasHoldemManager

def main():
    game   = TexasHoldemManager()
    app_on = True

    while app_on:
        print("  ~~~~~ TOMBSTONE POKER ~~~~~")
        print("  'Say when.' — Doc Holliday")

        choice = input("  --> ").strip().lower()

        if choice in ["1", "texas", "holdem"]:
            game.play_game()
        elif choice in ["2", "quit", "q"]:
            app_on = False

if __name__ == "__main__":
    main()
```

Daniel's 3-section pattern:
1. **Imports at the top** — grab what we need from other files
2. **`def main()`** — all the logic lives inside this function
3. **`main()` at the bottom** — `if __name__ == "__main__"` is the professional version

The `while app_on` loop keeps the menu running.
When the player picks Quit, `app_on = False` and the loop ends.
`app_on` is a **boolean flag** — Daniel taught this on Day 5 of Python 1.

---

## How It All Connects (The Import Chain)

```
You run: python main.py
  main.py loads → imports TexasHoldemManager from manager.py
    manager.py loads → imports CmpPlayer, HmnPlayer from players.py
    manager.py loads → imports Deck from deck.py
      deck.py loads → imports Card from card.py
```

Python follows this chain automatically before any game code runs.

---

## Every Class Concept From Daniel — Where It Shows Up

| What Daniel Taught | Where It Is In This Code |
|--------------------|--------------------------|
| `class ClassName:` | Card, Deck, CmpPlayer, TexasHoldemManager |
| `__init__(self, ...)` | Every class — the setup function |
| `self.attribute = value` | Every `__init__` — storing data on the object |
| `__repr__` | Card class — controls how it prints |
| `__str__` | Card class — controls f-string display |
| Class-level constants | `RANK_VALUES`, `RANKS`, `SUITS`, `COMP_NAMES` |
| Inheritance `Child(Parent)` | `HmnPlayer(CmpPlayer)` |
| Overriding a method | `decide_action()` in HmnPlayer replaces CmpPlayer's version |
| Polymorphism | Same `decide_action()` call → different result based on type |
| Multi-file imports | All 5 files linked with `from X import Y` |
| Dictionaries | `RANK_VALUES`, `value_counts`, `suit_counts` |
| Lists | `hand`, `cards`, `players`, `community_cards` |
| For loops | Building the deck, dealing, betting rounds |
| Nested for loops | Building all 52 cards in deck.py |
| While loops | `while app_on`, `while game_on` |
| Boolean flags | `app_on`, `game_on`, `player.folded` |
| f-strings | Every print statement |
| `.pop()` | `deck.deal()` removes and returns the top card |
| `random.shuffle()` | `deck.reset()` shuffles the cards |
| List comprehensions | Filtering active players, building value lists |
| `if __name__ == "__main__"` | main.py — the professional entry point Daniel mentioned |

---

## What To Say If Daniel Asks

**"Walk me through the Card class."**
> Card has three attributes: rank, suit, and value. Value is looked up from a class-level
> dictionary called RANK_VALUES that maps rank names to numbers — so Ace is 14, King is 13,
> and so on. That way I can compare cards mathematically. `__init__` sets those three
> attributes when you create a card. `__repr__` makes it print readable instead of showing
> a memory address.

**"How does inheritance work in your players?"**
> CmpPlayer is the base class — it has all the attributes and the computer decision logic.
> HmnPlayer is a subclass — it inherits everything from CmpPlayer but overrides just
> `decide_action` so it asks the player to type instead of auto-deciding. The game manager
> loops through all players and calls `decide_action()` on each one without checking what
> type it is. That's polymorphism — same call, different behavior.

**"How does hand evaluation work?"**
> I count how many of each card value appears using a dictionary, and how many of each suit.
> Then I check for hand types from best to worst — straight flush down to high card — and
> return a score number and a hand name. The player with the highest score wins.

**"Why Texas Hold'em?"**
> I like the movie Tombstone. Doc Holliday plays poker in it and I wanted to build something
> I actually cared about. It uses a standard 52-card deck and needs the same structure you
> showed us — Card, Deck, Players, Manager, Main. I figured if I was going to spend the time
> on it, I'd build something I'd actually want to play.

**"Why multiple files?"**
> Same reason you split blackjack into separate files — if I want to change how the Deck
> works, I only touch deck.py. The other files don't break. It also makes it way easier
> to find things when the project gets bigger.

---

## The Tombstone Connection

The computer players at the table are named after Tombstone characters:
Doc, Virgil, Morgan, Wyatt, Turkey Creek, Texas Jack.

The fold quotes rotate randomly — when someone folds, the game throws out a Doc Holliday line.
When someone wins, you get "You're no daisy at all." When someone goes broke, it quotes
"It appears the strain was more than he could bear."

That's why I built this game. I like Tombstone.

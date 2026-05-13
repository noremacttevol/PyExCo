# Classes and Objects (OOP)

**Status:** 🟡 Learning
**Project Used In:** Card Games (Blackjack / Texas Hold'em)
**Date Learned:** 2026-04-28
**Course Day:** Python 2, Day 1–2

---

## The Electrician's Analogy

A **class** is a **wiring diagram (schematic symbol)** for a piece of equipment. A **motor starter** has a known schematic symbol — three contacts, an overload, a coil. That symbol (the class) tells you what every motor starter looks like and how it behaves.

An **object** (also called an **instance**) is the actual physical motor starter installed in panel 3A. Same schematic, real hardware.

- **Class definition** (`class`) = drawing the schematic symbol once
- **Instance creation** = ordering and installing the actual hardware
- **Attributes** = the nameplate data on the starter (voltage rating, FLA, catalog number) — properties of that specific unit
- **Methods** = the behaviors of the starter (energize coil, trip on overload, reset) — what it can DO

You draw the schematic once. You install 12 identical starters throughout the plant using that same schematic. Each starter is its own object with its own runtime data (its own amps, its own trip history).

---

## What It Actually Does

A class is a blueprint that defines:
1. What **data** objects of this type will hold (attributes)
2. What **actions** objects of this type can perform (methods)

You define the class once, then create as many instances as you need. Each instance is independent — changing one doesn't affect the others.

---

## The Syntax (The Wire Diagram)

```python
# CLASS DEFINITION — the blueprint
class Card:

    # __init__ is the "constructor" — runs automatically when you create a new instance
    # self = "this specific object" — always the first parameter in every method
    def __init__(self, rank="Two", suit="Clubs"):
        # Attributes — data stored on this specific instance
        self.rank = rank   # self.rank is NOT the same as the parameter 'rank'
        self.suit = suit   # self.suit is stored on this object permanently

    # __repr__ — controls what prints when you print the object
    def __repr__(self):
        return f"[{self.rank} of {self.suit}]"

    # __eq__ — controls how == comparison works between two objects
    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit


# CREATING INSTANCES — using the blueprint to make real objects
card1 = Card("Ace", "Spades")     # Card() calls __init__ with those arguments
card2 = Card("King", "Hearts")
card3 = Card()                     # Uses defaults: Two of Clubs

# Accessing attributes
print(card1.rank)   # → "Ace"
print(card1.suit)   # → "Spades"
print(card1)        # → [Ace of Spades]  (uses __repr__)

# Each instance is independent
card1.rank = "Queen"   # Only changes card1, card2 is untouched
```

---

## The Full Architecture Pattern (Daniel's Approach)

Daniel splits everything into separate files:

| File | What It Contains |
|------|-----------------|
| `card.py` | `Card` class — one card, its rank and suit |
| `deck.py` | `Deck` class — a collection of Card objects, shuffle/draw |
| `players.py` | Player classes — hand management, score calculation, actions |
| `gameManager.py` | Game manager class — controls the whole game flow |
| `main.py` | Menu and entry point — imports everything, calls the manager |

Each class is one file. One responsibility per file. This is how real software is built.

---

## Key Dunder Methods (Double Underscore = "Magic Methods")

| Method | When it fires | What to put in it |
|--------|--------------|-------------------|
| `__init__` | When you create a new instance | Set up all attributes |
| `__repr__` | When you `print()` the object | Return a readable string |
| `__eq__` | When you use `==` to compare two objects | Return True/False |

---

## When You Use It

- Any time you need multiple "things" with the same structure (52 cards, 4 players, multiple motors)
- When an entity has both **data** (attributes) and **behavior** (methods) that belong together
- Python 2 projects — Daniel expects OOP structure from here forward

---

## Common Mistakes

- **Forgetting `self` as the first parameter:** Every method inside a class must have `self` as the first parameter. Without it → `TypeError`.
- **`self.attribute` vs local variable:** `self.rank` is stored on the object and persists. `rank` inside a method is a local variable that disappears when the method ends.
- **Calling `__init__` directly:** You never call `__init__` yourself — Python calls it automatically when you do `Card("Ace", "Spades")`.
- **Confusing class and instance:** `Card` is the blueprint. `card1 = Card(...)` is the actual object. You can't do `Card.rank` — you need an instance.

---

## Related Concepts
- [[Inheritance and Polymorphism]]
- [[Dictionaries]]
- [[Lists]]
- [[Modules and Imports]]

---
**Tags:** #python #python2 #oop #classes #objects #card-games #day-py2-1

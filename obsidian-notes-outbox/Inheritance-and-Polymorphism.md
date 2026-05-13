# Inheritance and Polymorphism

**Status:** 🟡 Learning
**Project Used In:** Card Games (Blackjack / Texas Hold'em)
**Date Learned:** 2026-04-28
**Course Day:** Python 2, Days 1–4

---

## The Electrician's Analogy

### Inheritance = Motor Starter Family

Allen-Bradley has a base **motor starter** — it has an overload, a contactor, basic wiring points. That's the **parent class**.

They also make a **reversing starter** — it's still a motor starter (inherits everything), but it adds a second contactor and a mechanical interlock so it can run in both directions. That's the **child class / subclass**.

The reversing starter doesn't re-invent the overload relay. It just **inherits** it from the base starter and adds what's new on top.

```
[Motor Starter — Parent]
    ├── Main contactor
    ├── Overload relay
    └── Basic terminals

    [Reversing Starter — Child]  ← inherits everything above
        └── Forward contactor (inherited)
        └── Reverse contactor (NEW)
        └── Mechanical interlock (NEW)
```

### Polymorphism = Same Rung Tag, Different Hardware

You have a PLC rung that calls `FWD_START` on whatever starter is connected to that I/O point. For one machine it's a basic starter. For another it's a reversing starter. The **rung doesn't care** — it calls `FWD_START` and the hardware figures out what that means for its own type.

Same function name, different behavior depending on the object type. That's polymorphism.

---

## What It Actually Does

**Inheritance:** A child class automatically gets all the attributes and methods of its parent class, and can add new ones or override existing ones.

**Polymorphism:** Multiple classes can have a method with the same name. Python calls the right version based on what type of object it is. The calling code doesn't need to know what type it's dealing with.

---

## The Syntax (The Wire Diagram)

```python
# PARENT CLASS (the base motor starter)
class BlackJackPlayer:
    VALUES = {"Two": 2, "Three": 3, "Ten": 10, "Jack": 10, "Ace": 11}

    def __init__(self, name="Bob"):
        self.name = name
        self.hand = []
        self.score = 0

    def draw(self, card):
        self.hand.append(card)

    def calcScore(self):
        self.score = sum(self.VALUES[card.rank] for card in self.hand)

    # This method will be OVERRIDDEN by the child class
    def chooseAction(self):
        self.calcScore()
        if self.score >= 17:
            return "stay"
        else:
            return "hit"

    def __repr__(self):
        return f"{self.name}"


# CHILD CLASS (inheriting from BlackJackPlayer — the reversing starter)
class HumBlackJackPlayer(BlackJackPlayer):  # ← parent class goes in parentheses
    # We only write what's DIFFERENT from the parent
    # draw(), calcScore(), __repr__, etc. are all inherited automatically

    # OVERRIDE chooseAction — same name, different behavior (POLYMORPHISM)
    def chooseAction(self):
        self.calcScore()
        if self.score >= 21:
            return "stay"
        else:
            # Human needs to see their hand and make a real choice
            self.showHand()
            choice = input("Hit or Stay? ").lower()
            return choice   # Returns what the human typed


# USING POLYMORPHISM IN THE GAME MANAGER
players = [BlackJackPlayer("Angela"), HumBlackJackPlayer("Cameron")]

for player in players:
    action = player.chooseAction()   # Same call on every player
    # For Angela (computer): just calculates automatically
    # For Cameron (human): shows hand, asks for input
    # The game manager doesn't need to know which type it's dealing with
```

---

## Key Rules

| Rule | What It Means |
|------|--------------|
| `class Child(Parent):` | Child inherits everything from Parent |
| Inherited methods just work | No need to copy-paste them into the child |
| Override by redefining | Write a method with the same name in the child — Python uses the child's version |
| `isinstance(obj, ClassName)` | Checks if an object is of a certain class type |
| `self.__class__` | Refers to whatever class `self` actually is at runtime |

---

## When You Use It

- **Inheritance:** When two things are "the same but different" — computer player vs human player, basic card game vs specific card game
- **Polymorphism:** When your game manager loop needs to call the same method on different types of players without checking which type they are
- Daniel's architecture: `BlackJackPlayer` is the parent, `HumBlackJackPlayer` is the child — only `chooseAction` is overridden

---

## Common Mistakes

- **Forgetting to call `super().__init__()`:** If your child class needs to run the parent's `__init__` code AND add to it, you need `super().__init__()` inside the child's `__init__`. If you skip it, the parent's attributes won't be set up.
- **Accidentally overriding when you didn't mean to:** If you name a method in the child the same as one in the parent, you override it. Be intentional about which methods you're replacing.
- **Thinking child classes get everything automatically:** They do get attributes and methods — but only if `__init__` sets them up properly. If the child has its own `__init__` without `super()`, it loses the parent's attribute setup.

---

## Related Concepts
- [[Classes and Objects]]
- [[Loops — While and For]]
- [[Dictionaries]]

---
**Tags:** #python #python2 #oop #inheritance #polymorphism #card-games #day-py2-1 #day-py2-4

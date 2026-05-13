# Program Structure — The 3-Section Pattern

**Status:** 🟢 Mastered
**Project Used In:** Calculator, Rock-Paper-Scissors, List Manager, Card Games
**Date Learned:** 2026-04-13
**Course Day:** Day 4

---

## The Electrician's Analogy

This is your **panel layout standard**. Every commercial panel has a logical layout: incoming power and main breakers at the top, branch circuits in the middle, load connections at the bottom. Nobody puts the main disconnect at the bottom and the load terminals at the top — it's a standard that makes every panel readable.

Daniel's 3-section pattern is the same thing for Python programs:

```
┌─────────────────────────────────────────┐
│ SECTION 1 — Incoming & Branch Circuits  │
│   imports, constants, helper functions  │
├─────────────────────────────────────────┤
│ SECTION 2 — Main Panel Logic            │
│   def main(): — all program logic       │
├─────────────────────────────────────────┤
│ SECTION 3 — Main Disconnect (Entry)     │
│   main()  — the call that starts it all │
└─────────────────────────────────────────┘
```

---

## What It Actually Does

This is the **standard layout** Daniel wants on every program. It keeps code organized, readable, and testable. Helper functions go on top (defined before they're used), all main program logic lives inside `main()`, and `main()` is called once at the bottom.

---

## The Syntax (The Wire Diagram)

```python
# ── SECTION 1: Imports & Helper Functions ──────────────────
from random import randint
import os

FILENAME = "savedlist.txt"   # Constants in UPPER_CASE

def helper_function_one(arg):
    # Small, single-purpose function
    return arg * 2

def helper_function_two():
    print("Helper doing a thing")


# ── SECTION 2: Main Function ────────────────────────────────
def main():
    running = True
    while running:
        # All your program logic lives here
        # Calls helper functions as needed
        helper_function_two()

        choice = input("Continue? (y/n): ")
        if choice == "n":
            running = False


# ── SECTION 3: Main Call ───────────────────────────────────
main()
# In more advanced programs: if __name__ == "__main__": main()
```

---

## When You Use It

Every program. This is the default layout. Follow it on every assignment unless Daniel specifically shows something different.

The `if __name__ == "__main__"` version (seen in list_manager.py) is the professional upgrade to the plain `main()` call — it means "only run this if this file is the one being executed directly, not if it's being imported by another file."

---

## Common Mistakes

- **Calling `main()` before defining it:** Python reads top-to-bottom. If `main()` is called before it's defined, you get a `NameError`. The call always goes last.
- **Putting all logic outside of functions:** Code at the module level (not inside a function) runs immediately when imported — which breaks multi-file projects.
- **Putting the dispatch dictionary inside the while loop:** Creates it fresh every iteration, wastes memory. Define it once outside the loop.

---

## Related Concepts
- [[Functions]]
- [[Modules and Imports]]
- [[Loops — While and For]]
- [[Dictionaries]]

---
**Tags:** #python #python1 #program-structure #best-practices #day4

# Lists

**Status:** 🟢 Mastered
**Project Used In:** List Manager, Card Games
**Date Learned:** 2026-04-14
**Course Day:** Day 5

---

## The Electrician's Analogy

A list is a **terminal strip** — a row of numbered positions on a DIN rail, each one holding exactly one value.

- Position 0 is the first terminal on the left (not 1 — electricians label them 0-indexed in Python)
- Position -1 is the last terminal on the right (Python lets you count from the end)
- Adding to the list (`.append()`) = snapping a new terminal block onto the right end of the strip
- Removing from the list (`.pop()`) = removing a terminal block by its position number

The terminal strip is **ordered** — T1 is always before T2. And unlike a dictionary (labeled terminals), these are **numbered positions only**.

---

## What It Actually Does

A list holds multiple values in a single variable, in a specific order. Each item has an **index** (position number) starting at 0. You can add, remove, sort, and access items by their index.

---

## The Syntax (The Wire Diagram)

```python
# Creating a list
motors = ["Motor 1A", "Motor 2B", "Motor 3C", "Motor 4D"]
#          index 0      index 1     index 2     index 3

# Accessing by index (zero-indexed)
motors[0]    # → "Motor 1A"   (first item)
motors[-1]   # → "Motor 4D"   (last item — negative counts from end)
motors[2]    # → "Motor 3C"

# Slicing — grab a range  [start:stop]  stop is EXCLUSIVE
motors[0:2]  # → ["Motor 1A", "Motor 2B"]   (index 0 and 1, NOT 2)
motors[::-1] # → reversed list

# Common methods
motors.append("Motor 5E")         # Add to end
motors.insert(1, "Motor 1B")      # Insert at index 1, shift everything right
motors.remove("Motor 2B")        # Remove by value (first occurrence)
motors.pop(0)                     # Remove and return item at index 0
motors.sort()                     # Sort alphabetically/numerically in place
len(motors)                       # How many items in the list

# Checking membership
if "Motor 3C" in motors:
    print("Found it")

# Nested lists (list of lists)
panel = [["Motor 1A", "Motor 2B"], ["Motor 3C", "Motor 4D"]]
panel[0][1]   # → "Motor 2B"  (first sub-list, second item)
```

---

## When You Use It

- Storing a collection of similar things (deck of cards, list of players, menu options)
- Iterating with a for loop — lists and loops are a matched pair
- Building the card deck: a list of Card objects
- The List Manager assignment: loading/saving a list to a file

---

## Common Mistakes

- **Zero-indexed:** First item is `[0]`, not `[1]`. Forgetting this causes off-by-one errors.
- **Slicing stop is exclusive:** `motors[0:2]` gives index 0 and 1. Not 2. People expect 3 items and get 2.
- **`IndexError`:** Accessing an index that doesn't exist crashes. If the list has 4 items, `motors[4]` crashes — max valid index is 3.
- **By-element for loop gives a copy:** `for motor in motors: motor = "X"` does NOT change the list. You need the index style to modify items.
- **`.remove()` removes the first occurrence only** — if the value appears twice, only the first gets removed.

---

## Related Concepts
- [[For Loops]]
- [[While Loops]]
- [[Dictionaries]]
- [[File I/O]]

---
**Tags:** #python #python1 #lists #data-structures #day5 #list-manager

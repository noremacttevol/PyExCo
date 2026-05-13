# Loops — While and For

**Status:** 🟢 Mastered
**Project Used In:** Calculator, List Manager, Card Games
**Date Learned:** 2026-04-14
**Course Day:** Day 5

---

## The Electrician's Analogy

### While Loop = Seal-in Circuit with a Stop Button

A while loop is a **latching relay with a seal-in contact**. When you hit Start, the relay coil energizes and seals itself in — it keeps itself energized through its own auxiliary contact. It runs continuously until you hit Stop (a condition turns False) and opens the seal-in contact.

```
[START]─┬──────────────────────( MOTOR RUN COIL )
        │
[MOTOR CONTACT]──────────────── (seal-in)
        │
[STOP ]─(NC)
```

The `running = True` flag is that seal-in contact. Set it to `False` and the loop falls out.

### For Loop = Scheduled PM Work Order

A for loop is like running a **Preventive Maintenance checklist** on every motor in a panel. You have a known list: Motor 1, Motor 2, Motor 3. You go to each one, do the same tasks, check it off, move to the next. You don't come back until the list is exhausted.

---

## What It Actually Does

**While loop:** Repeats as long as a condition is True. Use when you don't know how many times it needs to run — like keeping a menu open until the user quits.

**For loop:** Repeats a fixed number of times — once per item in a list, or for each number in a range. Use when you know the count or have a collection to iterate over.

---

## The Syntax (The Wire Diagram)

```python
# ── WHILE LOOP ──────────────────────────────────────────────
running = True   # Seal-in contact — ON

while running:   # "Keep going while this is True"
    choice = input("Menu: (1) Continue  (2) Quit: ")
    if choice == "2":
        running = False   # Opens the seal-in — loop ends

# break — emergency stop, exits loop immediately
while True:
    user = input("Type 'quit': ")
    if user == "quit":
        break   # Jumps out of the loop entirely

# continue — skip the rest of this pass, go to next iteration
for i in range(10):
    if i % 2 == 0:
        continue   # Skip even numbers
    print(i)       # Only prints 1, 3, 5, 7, 9


# ── FOR LOOP ────────────────────────────────────────────────
motors = ["Motor 1A", "Motor 2B", "Motor 3C"]

# Style 1 — by INDEX (you need the position number)
for i in range(len(motors)):
    print(f"{i}: {motors[i]}")   # Has the index, can modify the list

# Style 2 — by ELEMENT (cleaner, but no index)
for motor in motors:
    print(motor)   # Cleaner, but can't modify the original list this way

# range() — generates a sequence of numbers
range(5)         # 0, 1, 2, 3, 4
range(2, 6)      # 2, 3, 4, 5  (stop is exclusive)
range(0, 10, 2)  # 0, 2, 4, 6, 8  (step of 2)

# len() — number of items in a container
len(motors)   # → 3
```

---

## When You Use It

- **While loop:** Main program loops (keep the menu running), any "keep going until the user says stop" scenario
- **For loop (by element):** When you just need to read/use each item — printing, checking values
- **For loop (by index):** When you need to modify items, or need to know which position you're at (like displaying numbered lists: "1. Motor 1A")

---

## Common Mistakes

- **Infinite while loop:** Forgetting to update the condition inside the loop — `running` never becomes False, program hangs. Always make sure there's a path to exit.
- **By-element for loop can't modify the original list:** `for item in mylist: item = "X"` only changes the local copy. Use index style to actually change the list.
- **`range()` stop is exclusive:** `range(1, 4)` gives 1, 2, 3 — not 4. Matches how list slicing works.
- **Off-by-one in display vs index:** Display numbers start at 1 (humans), indices start at 0 (Python). When displaying `i + 1` and using `pop(i - 1)`, be consistent.
- **`break` exits the whole loop. `continue` only skips the current iteration.** Mixing these up causes logic errors.

---

## Related Concepts
- [[Lists]]
- [[Conditionals]]
- [[Boolean Flag Pattern]]
- [[File I/O]]

---
**Tags:** #python #python1 #loops #while #for #range #day5 #day6

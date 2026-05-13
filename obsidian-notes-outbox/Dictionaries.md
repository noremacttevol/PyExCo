# Dictionaries

**Status:** 🟢 Mastered
**Project Used In:** Calculator (dispatch table), Card Games (card values)
**Date Learned:** 2026-04-14
**Course Day:** Day 5

---

## The Electrician's Analogy

A dictionary is a **labeled terminal block** instead of a numbered one.

Instead of Terminal 0, Terminal 1, Terminal 2 — you have terminals labeled "L1", "L2", "GND", "24V+", "24V-". You look up a terminal by its **label** (key), not its position number.

A list is your numbered terminal strip. A dictionary is your labeled junction box with custom tags on each terminal.

- **Key** = the label on the terminal (must be unique — no two terminals with the same label)
- **Value** = the wire landed on that terminal (can be any type of data)

The dispatch table (Calculator 2.0) is like a **function selector switch** — you turn the key to "+", "-", "*", or "/" and it routes power to the right function block automatically. No need to check each position with an if/elif chain.

---

## What It Actually Does

A dictionary stores data as **key-value pairs**. You look up data by key (a name/label), not by position number. Keys must be unique. Values can be anything — strings, numbers, lists, even functions.

---

## The Syntax (The Wire Diagram)

```python
# Creating a dictionary
motor = {
    "tag": "Motor 3A",
    "voltage": 480,
    "amps": 12.5,
    "running": True
}

# Accessing by key
motor["tag"]       # → "Motor 3A"
motor["voltage"]   # → 480

# Adding or updating a key
motor["hp"] = 7.5             # Adds new key "hp"
motor["voltage"] = 460        # Updates existing key

# Checking if a key exists before accessing
if "hp" in motor:
    print(motor["hp"])

# Dictionary methods
motor.keys()     # → all key names
motor.values()   # → all values
motor.items()    # → all key-value pairs as tuples

# Dispatch table pattern — storing function references as values
def add(a, b):     return a + b
def subtract(a, b): return a - b

operations = {
    "+": add,        # The value IS the function (no parentheses = reference, not call)
    "-": subtract
}

# Calling the function stored at a key
result = operations["+"](10, 5)   # → 15
# operations["+"] retrieves the 'add' function
# (10, 5) then calls it with those arguments
```

---

## When You Use It

- Mapping something to something else (operator symbol → function, card rank → point value)
- Representing an object with named attributes (motor with tag, voltage, amps)
- **Dispatch tables** — replacing a long if/elif chain with a dictionary lookup
- Card game: card rank → numeric value (`{"Ace": 11, "King": 10, "Two": 2}`)

---

## Common Mistakes

- **Accessing a key that doesn't exist:** `motor["phase"]` if "phase" isn't in the dict → `KeyError`. Check with `in` first or use `.get()`.
- **Keys must be unique:** Assigning the same key twice overwrites the first value silently.
- **Function references vs calls:** `operations = {"+": add()}` is wrong — `add()` calls the function and stores the result. You want `"+": add` (no parentheses) to store the reference.
- **Dictionaries are not ordered by default in older Python** — in Python 3.7+ they maintain insertion order, but don't rely on it for position-based access.

---

## Related Concepts
- [[Lists]]
- [[Functions]]
- [[For Loops]]
- [[Classes and Objects]]

---
**Tags:** #python #python1 #dictionaries #data-structures #dispatch-table #day5 #day6

# Variables and Data Types

**Status:** 🟢 Mastered
**Project Used In:** Calculator
**Date Learned:** 2026-03-31
**Course Day:** Day 2

---

## The Electrician's Analogy

A **variable** is a terminal block position on a DIN rail. The label on the terminal (the name) is how you find it on the drawing. The wire landed on it (the value) is what's actually stored there.

- **Declaring a variable** = drilling the DIN rail and snapping in a new terminal block, giving it a label
- **Assigning a value** = landing a wire on that terminal
- You can pull the wire and land a different one — the terminal stays the same, the connection changes

**Data types** are like the different ratings on those terminals — you wouldn't land a 480V conductor on a 24VDC control terminal. Same idea: put the right type of data in the right variable.

| Type | Electrical Equivalent |
|------|----------------------|
| `int` | A whole-number setpoint (like 60 Hz) |
| `float` | A 4–20 mA analog signal with decimal precision |
| `str` | A text label on an HMI tag |
| `bool` | A pilot light — ON or OFF, nothing in between |
| `None` | An unused terminal — labeled but nothing landed |

---

## What It Actually Does

Variables store a value under a name so you can use it later. Without variables, every number or piece of text would be hardcoded — you'd have to hunt through the whole program to change anything.

Data types tell Python what kind of data you're storing so it knows what operations make sense on it (you can do math on a number, not on a string).

---

## The Syntax (The Wire Diagram)

```python
# Assigning values — the = is the wire landing, not a comparison
motor_speed = 1750        # int — whole number RPM
voltage = 480.0           # float — decimal
motor_tag = "Motor 3A"   # str — text, must be in quotes
is_running = True         # bool — capital T, not 'true'
fault_code = None         # None — empty, nothing there yet

# Python figures out the type automatically (dynamic typing)
# Check the type with type()
print(type(motor_speed))  # → <class 'int'>
```

---

## When You Use It

Every program. Variables are the wiring of your program — without them, nothing connects to anything else. You use them to:
- Store user input before doing math on it
- Keep track of scores, totals, states
- Pass data between functions

---

## Common Mistakes

- **Forgetting quotes on strings:** `name = Cameron` → Python thinks `Cameron` is another variable. Crashes with `NameError`.
- **Mixing `=` and `==`:** `=` assigns (lands the wire). `==` compares (checks if two things match). Using `=` inside an `if` is a wiring error.
- **`True`/`False` must be capitalized:** `true` is not valid Python — `NameError`.
- **Numbers in quotes:** `"480"` is a string, not a number. Math won't work on it until you typecast it.
- **Variable names can't start with a number:** `3phase = True` crashes. Use `phase_3 = True`.

---

## Related Concepts
- [[Typecasting]]
- [[F-strings]]
- [[Input and Output]]

---
**Tags:** #python #python1 #variables #data-types #day2

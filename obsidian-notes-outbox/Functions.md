# Functions

**Status:** 🟢 Mastered
**Project Used In:** Calculator
**Date Learned:** 2026-04-01
**Course Day:** Day 3

---

## The Electrician's Analogy

A function is a **PLC function block** — like a TON timer or a PID loop block.

- **Defining the function** (`def`) = wiring up the function block once in your program, giving it a tag name, setting its inputs
- **Parameters** = the input terminals on the block (IN, Preset, etc.)
- **Arguments** = the actual signal values you wire to those terminals when you call it
- **Return value** = the output terminal (OUT, Done bit, etc.) — the result that comes out the other side
- **Calling the function** = energizing the rung that triggers the function block to execute

You wire the block once, then you can trigger it from 10 different rungs. You don't re-wire it each time — you just call it. Same with functions.

Writing the function doesn't run it. You have to **call** it to make it execute — just like the function block doesn't run until that rung goes True.

---

## What It Actually Does

A function is a named, reusable block of code. You define it once with `def`, then call it by name whenever you need it. It can accept inputs (parameters) and send back a result (return value).

Without functions, you'd paste the same code over and over. With functions, you write it once and call it anywhere.

---

## The Syntax (The Wire Diagram)

```python
# DEFINING the function (wiring the function block — nothing runs yet)
def calculate_power(voltage, current):
    # Parameters are local variables inside this block
    watts = voltage * current
    return watts   # Send the result back to whoever called it

# CALLING the function (energizing the rung)
result = calculate_power(480, 12.5)   # Arguments: 480 → voltage, 12.5 → current
print(result)   # → 6000.0

# Default parameters — if you don't pass an argument, it uses the default
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Cameron")          # → "Hello, Cameron!"
greet("Cameron", "Hey")   # → "Hey, Cameron!"
```

---

## When You Use It

- Any time you repeat the same logic more than once — write it as a function
- Organizing code into clear labeled blocks (like labeling rungs in a ladder program)
- Daniel's standard: every program has helper functions at the top, `main()` in the middle, `main()` call at the bottom

---

## Common Mistakes

- **Calling without parentheses:** `calculate_power` vs `calculate_power()` — the first just references the function, doesn't run it. No output, no error.
- **Forgetting `return`:** Without `return`, the function gives back `None`. If you're expecting a value and it's `None`, you forgot to return.
- **Code after `return` won't run:** `return` exits the function immediately. Anything below it in the same function is dead code.
- **Indentation:** The function body must be indented. Wrong indentation = `IndentationError` or code that runs in the wrong scope.

---

## Related Concepts
- [[Variables and Data Types]]
- [[F-strings]]
- [[Modules and Imports]]
- [[Dictionary as Dispatch Table]]

---
**Tags:** #python #python1 #functions #day3 #calculator

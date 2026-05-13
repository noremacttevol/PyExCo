# Try / Except (Error Handling)

**Status:** 🟢 Mastered
**Project Used In:** List Manager, Calculator
**Date Learned:** 2026-04-15
**Course Day:** Day 6 (intro) / Day 7 (full)

---

## The Electrician's Analogy

`try/except` is your **thermal overload relay**.

Without an overload: motor draws too much current, windings burn up, motor's dead. Program crashes, user loses all their data.

With an overload: motor draws too much current, the overload **trips** instead of letting the motor burn — it catches the fault, shuts down safely, and gives you a trip indicator you can read. Program hits a bad condition, `except` catches it, handles it gracefully, program keeps running.

You don't wire a motor without an overload. You don't write file I/O or type conversion without `try/except`.

```
[MOTOR]──[OVERLOAD RELAY]──( OUTPUT )
                │
                └──( TRIP INDICATOR )   ← this is your except block
```

---

## What It Actually Does

`try` wraps code that might fail. If it does fail, instead of crashing the whole program, Python jumps to the `except` block and runs that instead. You can catch specific error types or catch any error.

---

## The Syntax (The Wire Diagram)

```python
# Basic structure
try:
    # Code that might fail
    value = int(input("Enter a number: "))
except ValueError:
    # What to do when it fails with that specific error
    print("That wasn't a number — try again")

# Common error types to catch
# ValueError      — wrong type conversion (int("hello"))
# IndexError      — list index out of range (mylist[99])
# FileNotFoundError — opening a file that doesn't exist
# ZeroDivisionError — dividing by zero
# KeyError        — accessing a dict key that doesn't exist

# Catch multiple exception types
try:
    index = int(user_input) - 1
    items.pop(index)
except ValueError:
    print("Not a number")
except IndexError:
    print("Number out of range")

# Catch multiple in one line
except (ValueError, IndexError):
    print("Invalid selection")

# Nested try/except (from List Manager — handles both type AND range)
try:
    index = int(user_input)      # Could fail: ValueError (not a number)
    try:
        items.pop(index - 1)     # Could fail: IndexError (out of range)
    except IndexError:
        print("Number out of range")
except ValueError:
    # Not a number — treat as a string value to search by name
    try:
        items.remove(user_input)
    except ValueError:
        print("Item not found")

# File not found pattern
try:
    with open("savedlist.txt", "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    lines = []   # File doesn't exist yet — start fresh
```

---

## When You Use It

- Any `int()` or `float()` conversion of user input — users type wrong things constantly
- Any file read in `"r"` mode — file might not exist yet
- Any list index access where the index comes from user input
- Dictionary key access where the key might not be in the dict

---

## Common Mistakes

- **Catching too broadly:** `except Exception:` catches everything including bugs you should fix. Use specific error types.
- **Empty except block:** `except: pass` silently swallows errors — you'll never know something went wrong.
- **Forgetting to handle the error usefully:** Catching the error and doing nothing is almost as bad as crashing — at least print something helpful.
- **Putting too much code in the `try` block:** Only put the risky line(s) in `try`. Long `try` blocks make it hard to know what actually failed.

---

## Related Concepts
- [[File I/O]]
- [[Lists]]
- [[Input, Output, Typecasting, and F-strings]]

---
**Tags:** #python #python1 #try-except #error-handling #day6 #day7

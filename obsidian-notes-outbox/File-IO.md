# File I/O (Reading and Writing Files)

**Status:** 🟢 Mastered
**Project Used In:** List Manager
**Date Learned:** 2026-04-21
**Course Day:** Day 7

---

## The Electrician's Analogy

File I/O is like reading from and writing to **PLC data registers saved to EEPROM** — non-volatile memory that persists after power is cut.

Your program's variables are like **RAM** — when the program stops, all that data is gone. Writing to a file is like **saving setpoints to EEPROM or a historian** — the data survives a power cycle (a program restart).

- **`"r"` mode** = reading the historian — pulling saved values into the current scan
- **`"w"` mode** = overwriting the EEPROM block completely with new values — starts fresh
- **`"a"` mode** = appending to the historian log — adds new entries without erasing the old ones

The `with` statement is like a **circuit breaker with automatic trip protection** — the file handle (breaker) closes when you're done, automatically, even if something goes wrong. You don't have to manually close it.

---

## What It Actually Does

Python can read data from and write data to text files on your computer using `open()`. The data persists after the program ends, so you can save state between sessions.

---

## The Syntax (The Wire Diagram)

```python
# READING a file
with open("savedlist.txt", "r") as f:
    content = f.read()           # Entire file as one string
    # OR
    lines = f.readlines()        # List of lines — each ends with "\n"

# WRITING a file (overwrites everything — be careful)
with open("savedlist.txt", "w") as f:
    f.write("Motor 1A\n")        # Must add \n manually for newlines
    f.writelines(["item1\n", "item2\n"])  # Write a whole list at once

# APPENDING (adds to end, doesn't erase)
with open("log.txt", "a") as f:
    f.write("New log entry\n")

# The \n problem — readlines() includes the newline character
lines = f.readlines()
# lines = ["Motor 1A\n", "Motor 2B\n", "Motor 3C\n"]
# Strip it before using:
lines = [line.replace("\n", "") for line in lines]
# OR use .strip():
lines = [line.strip() for line in lines]
# → ["Motor 1A", "Motor 2B", "Motor 3C"]

# Handle missing file gracefully
try:
    with open("savedlist.txt", "r") as f:
        lines = f.readlines()
    items = [line.strip() for line in lines]
except FileNotFoundError:
    items = []   # File doesn't exist yet — start with empty list
```

---

## When You Use It

- Any time data needs to survive between program runs (saved lists, high scores, settings, logs)
- The List Manager: load from file on startup, save to file after every change
- Always use the `with` statement — it auto-closes the file so you don't have data corruption

---

## Common Mistakes

- **`"w"` mode erases everything first.** Using `"w"` when you meant `"a"` wipes your file. Check your mode before opening.
- **`"r"` crashes if file doesn't exist.** Always wrap reads in `try/except FileNotFoundError` or check with `os.path.exists()` first.
- **`readlines()` keeps the `\n`.** Always strip before using the values — otherwise you'll get `"Motor 1A\n"` instead of `"Motor 1A"`.
- **File saves next to your script.** If you run the script from a different folder, the file may appear somewhere unexpected.
- **Changes in memory don't auto-save.** You must call your save function explicitly after any modification. Python doesn't write to disk automatically.

---

## Related Concepts
- [[Lists]]
- [[Try/Except]]
- [[Loops — While and For]]
- [[List Manager App]]

---
**Tags:** #python #python1 #file-io #day7 #list-manager

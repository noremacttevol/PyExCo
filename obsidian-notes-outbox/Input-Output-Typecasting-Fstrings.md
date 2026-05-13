# Input, Output, Typecasting, and F-strings

**Status:** 🟢 Mastered
**Project Used In:** Calculator
**Date Learned:** 2026-04-01
**Course Day:** Day 3

---

## The Electrician's Analogy

**`print()`** is your **HMI panel display** — it pushes data to the screen so the operator (you) can read it.

**`input()`** is your **HMI keypad entry field** — the program pauses and waits for the operator to type something and hit Enter, then stores what they typed.

**Typecasting** is like converting signal types on a PLC — your 4–20 mA analog input comes in as a raw integer count (0–32767). If you want actual engineering units (0–100%), you have to **convert it**. Same idea: `input()` always gives you a string. If you need a number, you convert it.

**F-strings** are an **HMI display string with variable substitution** — instead of hardcoding "Motor running at 1750 RPM", the HMI pulls the live tag value and inserts it into the display text automatically.

---

## What It Actually Does

- **`print()`** — sends output to the terminal/screen
- **`input()`** — pauses the program, waits for keyboard input, always returns a **string** no matter what the user types
- **Typecasting** — converts data from one type to another (`int()`, `float()`, `str()`)
- **F-strings** — embed variables or expressions directly inside a string using `{}`

---

## The Syntax (The Wire Diagram)

```python
# print() — output to screen
print("Motor is running")
print(motor_speed)          # Works with any type

# input() — ALWAYS returns a string
user_input = input("Enter motor speed (RPM): ")
print(type(user_input))     # → <class 'str'>  ← even if they typed 1750

# Typecasting — converting to the right type before doing math
speed = int(input("Enter motor speed: "))   # "1750" → 1750
voltage = float(input("Enter voltage: "))   # "480.5" → 480.5

# int() conversion edge case — can't convert decimals directly
# int("3.14")   ← CRASHES with ValueError
# Do this instead:
value = int(float("3.14"))  # First to float, then to int → 3

# F-strings — put f before the opening quote, use {} for variables
motor = "Motor 3A"
speed = 1750
print(f"{motor} is running at {speed} RPM")
# → Motor 3A is running at 1750 RPM

# You can do math inside the braces
print(f"Next maintenance at {speed * 2} hours")
```

---

## When You Use It

- `print()`: Anytime you want to show output — results, menus, prompts
- `input()`: Anytime your program needs data from the user
- **Always typecast `input()` output before doing math** — it's a string, always
- F-strings: Any time you're building a display message that includes variable data

---

## Common Mistakes

- **`input()` returns a string — always.** Doing math on it without casting crashes with `TypeError`.
- **`int("3.14")` crashes** — can't convert a decimal string straight to int. Float first, then int.
- **`int("hello")` crashes** — can only cast if the value actually represents that type.
- **Forgetting the `f` before the string:** `"{name}"` just prints literally `{name}` — it's not an f-string unless you write `f"{name}"`.

---

## Related Concepts
- [[Variables and Data Types]]
- [[Functions]]
- [[Try/Except]]

---
**Tags:** #python #python1 #input #output #typecasting #fstrings #day3

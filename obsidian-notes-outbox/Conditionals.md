# Conditionals (if / elif / else)

**Status:** 🟢 Mastered
**Project Used In:** Calculator, Rock-Paper-Scissors
**Date Learned:** 2026-04-13
**Course Day:** Day 4

---

## The Electrician's Analogy

Conditionals are **relay ladder logic rungs with normally-open contacts in series**.

- `if` = the first NO contact — if that condition closes (True), current flows through the rung and the output coil fires
- `elif` = another contact further down the same rung, only checked if the one above it never closed
- `else` = a catch-all coil at the end — only energizes if **nothing** above it was True

PLC behavior: the scan goes top-to-bottom and stops at the first True rung. Everything below doesn't fire. Same in Python — first True condition wins, the rest are skipped.

```
[motor_temp > 100]──────────────────( SHUTDOWN )
[motor_temp > 80 ]──────────────────( ALARM    )
[ ALL ELSE       ]──────────────────( NORMAL   )
```

---

## What It Actually Does

Lets your program make decisions and branch to different code depending on whether a condition is True or False. One and only one branch runs.

---

## The Syntax (The Wire Diagram)

```python
motor_temp = 95

if motor_temp > 100:
    print("SHUTDOWN — motor overheating")
elif motor_temp > 80:
    print("ALARM — monitor closely")
elif motor_temp > 60:
    print("WARM — within limits")
else:
    print("Normal operating temperature")
# Only one of these prints — whichever condition is True first

# Comparison operators
# ==  equal to           (is this terminal at 24V?)
# !=  not equal to       (is this NOT the fault code I expect?)
# >   greater than
# <   less than
# >=  greater than or equal to
# <=  less than or equal to

# Logical operators — combining conditions
if voltage >= 460 and voltage <= 500:
    print("Voltage in range")

if phase == "A" or phase == "B":
    print("Checking phase A or B")

# The 'in' keyword — cleaner version of multiple 'or' checks
valid_choices = ["rock", "paper", "scissors"]
if user_choice in valid_choices:
    print("Valid input")
```

---

## When You Use It

- Validating user input (is what they typed a real option?)
- Branching game logic (who won? tie? computer?)
- Checking ranges or states (is this value in spec?)
- Any time your program needs to do different things based on a condition

---

## Common Mistakes

- **`=` vs `==`:** `if x = 5` is a syntax error. `=` assigns, `==` compares. Never mix them in a condition.
- **Order matters:** `elif` checks only if everything above it was False. If you check `> 60` before `> 80`, the `> 80` case will never be reached.
- **Missing colon:** Forgetting the `:` at the end of `if`, `elif`, or `else` → `SyntaxError`.
- **Indentation:** Code inside the `if` block must be indented consistently. Wrong indent = code runs in the wrong place or `IndentationError`.
- **`.lower()` before comparing:** User types "Rock", "ROCK", "rock" — if you compare directly, only "rock" matches. Always `.lower()` input before comparing.

---

## Related Concepts
- [[Comparison Operators]]
- [[Logical Operators]]
- [[While Loops]]
- [[Modules and Imports]]

---
**Tags:** #python #python1 #conditionals #control-flow #day4

# Concept Note Template

Use this exact format for every concept note. Save to `obsidian-notes-outbox/` with filename matching the concept (e.g., `Lists.md`).

```markdown
# [Concept Name]

**Status:** 🟢 Mastered / 🟡 Learning / 🔴 Not Started
**Project Used In:** [Calculator / Blackjack / etc.]
**Date Learned:** YYYY-MM-DD
**Course Day:** [Day N]

---

## The Electrician's Analogy
[How this Python concept maps to something Cameron already knows from the trade — relays, contactors, PLCs, motor starters, ladder logic, 3-phase, sawmill machinery, etc.]

## What It Actually Does
[Plain-English description. No jargon. No "as we know from computer science..."]

## The Syntax (The Wire Diagram)
\`\`\`python
# Code example with comments that explain WHY, not just WHAT
\`\`\`

## When You Use It
[Real scenarios where this concept solves a problem. Tie back to the project at hand if possible.]

## Common Mistakes
[Where the wires get crossed. What error messages look like. How to fix them.]

## Related Concepts
- [[Linked concept 1]]
- [[Linked concept 2]]

---
**Tags:** #python #[project-name] #[concept-type]
```

## Example Filled-Out Note (For Reference)

```markdown
# If/Elif/Else

**Status:** 🟢 Mastered
**Project Used In:** Calculator
**Date Learned:** 2025-XX-XX
**Course Day:** Day 3

---

## The Electrician's Analogy
If/Elif/Else is a **relay logic ladder rung with multiple contacts in series**.

- `if` is the first contact — if it's closed (True), the rung energizes and the output fires.
- `elif` is the next contact down the rung — only checked if the first one was open (False).
- `else` is the catch-all coil at the bottom — fires only if NONE of the contacts above closed.

Just like a PLC, Python checks each condition top-to-bottom and stops at the first True.

## What It Actually Does
Lets your program make decisions based on conditions. "If this is true, do this. Otherwise, check the next thing. Otherwise, do the default."

## The Syntax (The Wire Diagram)
\`\`\`python
temperature = 95

if temperature > 100:
    print("Motor is overheating - shut down")
elif temperature > 80:
    print("Motor is warm - monitor closely")
else:
    print("Motor temperature is normal")
\`\`\`

## When You Use It
Anywhere your program needs to branch — checking user input, validating data, deciding what to do next based on a value.

## Common Mistakes
- Forgetting the colon `:` at the end of the line — Python throws `SyntaxError`
- Using `=` (assignment) instead of `==` (comparison) inside the condition
- Inconsistent indentation — Python is strict about this; mixing tabs and spaces will break the rung

## Related Concepts
- [[Comparison Operators]]
- [[Boolean Logic]]
- [[Indentation]]

---
**Tags:** #python #calculator #control-flow
```

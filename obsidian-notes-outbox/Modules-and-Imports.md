# Modules and Imports

**Status:** 🟢 Mastered
**Project Used In:** Calculator, Rock-Paper-Scissors
**Date Learned:** 2026-04-13
**Course Day:** Day 4

---

## The Electrician's Analogy

A module is a **manufacturer's equipment catalog** — Allen-Bradley, Square D, Siemens. You don't design a new motor starter from scratch every time. You pull the one that fits your specs from the catalog, land it in the panel, and wire it in.

`import random` = pulling the `random` module from Python's standard catalog (it's already installed, just not active until you call it in)

`from random import randint` = ordering just the specific component you need (the `randint` function) instead of the whole catalog binder

The 5 import methods:

| Method | Electrical Equivalent |
|--------|----------------------|
| `import math` | Bring the whole Square D catalog, use it as `math.sqrt()` |
| `import math as m` | Same catalog, short-labeled as `m.sqrt()` on your drawings |
| `from math import sqrt` | Pull just the one component you need — no prefix needed |
| `from math import sqrt as sq` | Same component, give it your own tag name on the drawing |
| `from math import *` | Pull everything from the catalog into your panel — messy, risky |

---

## What It Actually Does

Modules are pre-written Python files full of useful functions and tools. Instead of writing everything from scratch, you import the module and use what's in it. Python comes with a huge **standard library** of modules (math, random, os, json, etc.), plus you can install third-party ones.

---

## The Syntax (The Wire Diagram)

```python
# Method 1 — import whole module, use dot notation
import math
result = math.sqrt(144)   # → 12.0

# Method 2 — alias (short name)
import math as m
result = m.sqrt(144)

# Method 3 — import just what you need (no dot notation)
from math import sqrt
result = sqrt(144)

# Method 4 — import with alias
from math import sqrt as square_root
result = square_root(144)

# Method 5 — wildcard (NOT recommended — causes naming conflicts)
from math import *
result = sqrt(144)   # Works, but risky

# Common modules in this course:
from random import randint    # Random integers
randint(1, 6)                  # Random number 1–6 inclusive (like rolling a die)

import os                      # Operating system tools
os.path.exists("myfile.txt")   # Check if a file exists
```

---

## When You Use It

- `random` — any time you need random numbers (card games, dice, RPS)
- `math` — square roots, trig, logarithms
- `os` — file path checking, directory operations
- Always placed at the **top of your file**, before any function definitions

---

## Common Mistakes

- **Name conflicts with wildcard imports:** If you `from math import *` and also write your own function called `sqrt`, Python will use your version and silently ignore the math one. Use Method 1 or 3 to avoid this.
- **Importing at the wrong place:** Imports go at the top of the file, not inside functions (unless there's a specific reason).
- **Forgetting dot notation with Method 1:** `import math` then calling `sqrt(16)` → `NameError`. You need `math.sqrt(16)`.
- **`randint` is inclusive on both ends:** `randint(1, 3)` can return 1, 2, **or 3**. That's different from most range functions.

---

## Related Concepts
- [[Functions]]
- [[Program Structure — 3-Section Pattern]]
- [[Random Module]]

---
**Tags:** #python #python1 #modules #imports #random #day4

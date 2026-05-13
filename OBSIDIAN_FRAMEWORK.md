# Obsidian Framework — PyExCo-Brain Vault

## Vault Name
`PyExCo-Brain`

## Folder Structure

```
PyExCo-Brain/
├── 00_Index/                  <- Master tracker, what you know vs what's missing
│   └── Knowledge-Tracker.md
├── 01_Concepts/               <- One note per Python concept
├── 02_Projects/
│   ├── Calculator/            <- Completed project notes
│   └── Blackjack/             <- Current project notes
├── 03_Transcripts/            <- Cleaned-up lecture content
├── 04_Analogies/              <- Master list of industrial analogies
└── 05_Cheatsheets/            <- Quick-reference syntax sheets
```

## The Knowledge Tracker (00_Index/Knowledge-Tracker.md)

This is the single source of truth for what Cameron has learned. Update it every session.

```markdown
# Python Knowledge Tracker

**Last Updated:** YYYY-MM-DD
**Current Project:** [Calculator / Blackjack / etc.]
**Current Day in Course:** [Day N]

---

## ✅ Mastered
- [[Variables]]
- [[Input/Output]]
- [[If/Elif/Else]]
- [[Functions - Basic]]
- [[Arithmetic Operators]]

## 🟡 Currently Learning
- [ ] [[Lists]]
- [ ] [[Random Module]]
- [ ] [[While Loops]]
- [ ] [[For Loops]]
- [ ] [[Functions - Return Values]]
- [ ] [[Dictionaries]]

## 🔴 Not Yet Touched
- [ ] Classes / Objects
- [ ] File I/O
- [ ] Try/Except (Error Handling)
- [ ] List Comprehensions
- [ ] Modules and Imports
- [ ] String Methods (advanced)

## 📋 Project Status
- **Calculator:** ✅ Complete
- **Blackjack:** 🟡 In progress

## 🧰 Analogies Built So Far
- See [[Analogy-Library]]
```

## Note Lifecycle

1. **New concept hit during work** → Generate note in `obsidian-notes-outbox/`
2. **Cameron drags note into Obsidian** → Lives in `01_Concepts/`
3. **Knowledge Tracker updated** → Status moves from 🔴 → 🟡 → 🟢

## Linking Strategy

Use Obsidian's `[[wiki-style links]]` aggressively. Every concept note should link to:
- Related concepts (e.g., a note on `For Loops` links to `[[Lists]]` and `[[Range]]`)
- Projects where it was used (e.g., `[[Blackjack]]`)
- The analogy entry (e.g., `[[Analogy-Library#Relay-Logic]]`)

This builds a graph view that visually shows Cameron's growing knowledge — like a one-line diagram of his Python understanding.

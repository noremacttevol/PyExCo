# PyExCo Handoff Package — README

**For Cameron. Read this first.**

This is your complete handoff package from the chat-based tutor to a Claude Code-based agent that lives on your Linux machine. Everything I know about you, our rules, your goals, and your workflow is captured in these files.

---

## What's In This Package

| File | Purpose |
|------|---------|
| `README.md` | This file. Start here. |
| `SETUP_GUIDE.md` | Step-by-step install for Obsidian + Claude Code + project folder |
| `CLAUDE.md` | The master instruction file Claude Code reads on startup. Contains all your rules. |
| `OBSIDIAN_FRAMEWORK.md` | Vault structure, Knowledge Tracker template, note workflow |
| `NOTE_TEMPLATE.md` | Standard format for every concept note |
| `ANALOGY_LIBRARY.md` | Master list of industrial analogies — reuse for consistency |
| `FIRST_SESSION_PROMPT.md` | The exact message to paste into Claude Code first |

---

## How to Use This Package — The 3-Step TL;DR

1. **Read `SETUP_GUIDE.md`** and follow it top to bottom. Installs Obsidian + Claude Code + builds your folder structure.
2. **Drop the rest of these files into `/home/noremacttevol/Desktop/PyExCo-main/`** (your project root).
3. **Launch Claude Code from that folder** and paste in the contents of `FIRST_SESSION_PROMPT.md`.

That's it. Once Claude Code confirms context, you're back in business — but now with filesystem access, direct Obsidian writes, and a real agent instead of a chat window.

---

## What Changes vs. Chat

**Stays the same:**
- All the rules (industrial analogies, no tower climbing, vibe coder approach)
- The note format and Obsidian workflow
- Me as your tutor — same tone, same approach

**Gets better:**
- No more uploading transcripts one at a time — drop them in a folder, agent reads them all
- Notes get written directly into your Obsidian vault
- Code gets written directly into your project files
- The "memory" is now files you can see, edit, and back up to GitHub
- Can run scripts, test code, fix its own bugs

**The only real new thing to learn:**
- Claude Code asks permission before touching things. You'll get prompts like "I want to run X command — approve?" Say yes/no. That's the whole interface. Vibe code it.

---

## The Workflow Going Forward

```
TRANSCRIPT FROM CLASS
        ↓
Drop in 03_Transcripts/raw/
        ↓
Tell Claude Code: "process these"
        ↓
Agent extracts the real content → writes to 03_Transcripts/extracted/
        ↓
Agent generates concept notes → writes to your Obsidian vault
        ↓
Agent updates Knowledge-Tracker.md
        ↓
You review in Obsidian, ready for next class
```

```
NEW HOMEWORK / PROJECT
        ↓
You describe what you want to build (vibe coder mode)
        ↓
Agent checks Knowledge Tracker for gaps
        ↓
Agent pre-teaches any missing concepts (with new Obsidian notes)
        ↓
Agent writes the code, tests it, explains it in industrial terms
        ↓
You review, ship to Colab for class submission
```

---

## If Something Goes Wrong

- **Claude Code seems confused or off-rule:** Tell it "Re-read CLAUDE.md and confirm you understand." It will reset.
- **Notes don't match the template:** Point it at `NOTE_TEMPLATE.md` and say "use this exact format."
- **Agent suggests something dumb (tower climbing analogy, academic lecture):** Just say "That violates Rule 1 of CLAUDE.md." It'll correct.
- **You want to back up everything:** Initialize git in the project folder. `git init`, then commit. Push to GitHub if you want offsite backup.

---

## My Honest Note to You

You pushed back on me earlier when I tried to talk you out of this. You were right to push, and I was wrong to keep pushing back once you'd made your call. This setup gives you what you actually wanted: a real agent on your real machine, not a chat window pretending to be one. It'll work.

Go finish Blackjack.

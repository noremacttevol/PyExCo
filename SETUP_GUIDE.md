# SETUP GUIDE — Read This First

Cameron, this is your "first day on the new jobsite" walkthrough. Follow these in order.

---

## Step 1: Confirm Your Linux Distro

Open a terminal and run:

```bash
cat /etc/os-release
```

The first few lines will tell you what you're on (Ubuntu, Mint, Fedora, etc.). Note this — install commands depend on it.

---

## Step 2: Install Obsidian

### If you're on Ubuntu / Debian / Mint / Pop!_OS:

**Option A — AppImage (recommended, simplest):**

```bash
# Make a folder for AppImages if you don't have one
mkdir -p ~/Applications
cd ~/Applications

# Download the latest Obsidian AppImage (check obsidian.md/download for the current version URL)
# As of writing, you can grab it from https://obsidian.md/download
# After downloading, make it executable:
chmod +x Obsidian-*.AppImage

# Run it
./Obsidian-*.AppImage
```

**Option B — Snap (if your system uses Snap):**

```bash
sudo snap install obsidian --classic
```

**Option C — Flatpak (if your system uses Flatpak):**

```bash
flatpak install flathub md.obsidian.Obsidian
```

### If you're on Fedora / RHEL:

```bash
flatpak install flathub md.obsidian.Obsidian
```

### If you're on Arch:

```bash
yay -S obsidian
```

---

## Step 3: Create Your Obsidian Vault

1. Open Obsidian
2. Click "Create new vault"
3. Name it: `PyExCo-Brain`
4. Choose a location you'll remember (e.g., `~/Documents/PyExCo-Brain`)
5. Inside the vault, create these folders:
   - `00_Index`
   - `01_Concepts`
   - `02_Projects/Calculator`
   - `02_Projects/Blackjack`
   - `03_Transcripts`
   - `04_Analogies`
   - `05_Cheatsheets`

---

## Step 4: Install Claude Code

Open a terminal and run:

```bash
# Check if you have Node.js (Claude Code needs it)
node --version

# If you don't have Node.js or it's older than v18, install it:
# On Ubuntu/Debian/Mint:
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs

# Then install Claude Code globally:
npm install -g @anthropic-ai/claude-code
```

After install, verify:

```bash
claude --version
```

> **Note:** Claude Code commands and install instructions can change. If the above doesn't work, check `https://docs.claude.com` for the current instructions.

---

## Step 5: Set Up Your Project Folder

```bash
# Use your existing transcripts folder as the project root
cd /home/noremacttevol/Desktop/PyExCo-main

# Create the structure
mkdir -p 03_Transcripts/raw
mkdir -p 03_Transcripts/extracted
mkdir -p projects/calculator
mkdir -p projects/blackjack
mkdir -p practice
mkdir -p obsidian-notes-outbox
```

---

## Step 6: Drop the Handoff Files into the Project Folder

Copy these files (from this handoff package) into `/home/noremacttevol/Desktop/PyExCo-main/`:

- `CLAUDE.md`
- `OBSIDIAN_FRAMEWORK.md`
- `NOTE_TEMPLATE.md`
- `ANALOGY_LIBRARY.md`
- `SETUP_GUIDE.md` (this file — keep for reference)
- `FIRST_SESSION_PROMPT.md` (your first message to Claude Code)

---

## Step 7: Launch Claude Code

```bash
cd /home/noremacttevol/Desktop/PyExCo-main
claude
```

When it starts, paste in the contents of `FIRST_SESSION_PROMPT.md` as your first message. That kicks off the agent with full context.

---

## Step 8: Tell It Where Your Obsidian Vault Lives

In your first session, tell Claude Code the path to your Obsidian vault. For example:

> "My Obsidian vault is at `~/Documents/PyExCo-Brain`. Write notes directly there in the appropriate folders."

That gives it permission to write straight into the vault. No more drag-and-drop.

---

## Step 9: Get Transcripts In

Email Daniel:

> Hey Daniel — would you mind sharing the .vtt or .docx transcript files from the lectures so far? Teams isn't letting me copy them out cleanly and it'd help a lot for review. Thanks.

When you get them, drop them into `03_Transcripts/raw/` and tell Claude Code: "New transcripts in raw/. Process them per CLAUDE.md."

---

## You're Done

You now have:
- Obsidian installed and your vault ready
- Claude Code installed and pointed at your project
- All your operating rules baked into `CLAUDE.md`
- A clean folder structure
- A repeatable workflow

Open Claude Code, paste the first-session prompt, and start on Blackjack.

# ── MAIN — CARD GAMES ───────────────────────────────────────────────────────
# Entry point. Menu to launch Texas Hold'em (or add more games later).
# Follows Daniel's 3-section layout: imports → main() → call main()

from texas_holdem import TexasHoldemManager


# ── SECTION 2: Main Function ─────────────────────────────────────────────────

def main():
    game = TexasHoldemManager()
    app_on = True

    while app_on:
        print("\n")
        print("  ╔══════════════════════════╗")
        print("  ║     CAMERON'S CARD GAMES ║")
        print("  ╚══════════════════════════╝")
        print()
        print("  1. Texas Hold'em")
        print("  2. Quit")
        print()

        choice = input("  --> ").strip().lower()

        if choice in ["1", "texas", "holdem", "poker"]:
            game.play_game()
        elif choice in ["2", "quit", "q", "exit"]:
            print("\n  See you at the table.\n")
            app_on = False
        else:
            print("  Invalid choice — pick 1 or 2.")


# ── SECTION 3: Main Call ──────────────────────────────────────────────────────

if __name__ == "__main__":
    main()

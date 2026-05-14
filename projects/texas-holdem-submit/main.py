# main.py
# Entry point for the Card Games app — Texas Hold'em edition.
# Follows Daniel's 3-section layout: imports, main(), then call main().

from manager import TexasHoldemManager


# ── SECTION 2: Main Function ──────────────────────────────────────────────────

def main():
    game   = TexasHoldemManager()
    app_on = True

    while app_on:
        print("")
        print("  ~~~~~ TOMBSTONE POKER ~~~~~")
        print("  'Say when.' — Doc Holliday")
        print("")
        print("  1. Texas Hold'em")
        print("  2. Quit")
        print("")

        choice = input("  --> ").strip().lower()

        if choice in ["1", "1.", "texas", "holdem"]:
            game.play_game()
        elif choice in ["2", "2.", "quit", "q"]:
            app_on = False
        else:
            print("  Invalid option — choose 1 or 2.")


# ── SECTION 3: Main Call ──────────────────────────────────────────────────────

if __name__ == "__main__":
    main()

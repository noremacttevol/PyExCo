# currency.py
# Models poker chips as an in-game currency.
# Built to go with the Texas Hold'em project — same chips, same table.

class Currency:

    CHIPS_PER_DOLLAR = 10   # 1 USD = 10 chips

    def __init__(self, amount=0):
        self.amount = int(amount)   # chips are whole numbers only

    # ── The Big 3 ─────────────────────────────────────────────────────────────

    def __repr__(self):
        return f"{self.amount} chips"

    def __str__(self):
        return self.__repr__()

    # ── Arithmetic ────────────────────────────────────────────────────────────

    def __mul__(self, other):
        return Currency(self.amount * other)

    def __truediv__(self, other):
        return Currency(int(self.amount / other))

    def __iadd__(self, other):
        # isinstance lets you add Currency + Currency or Currency + plain number
        if isinstance(other, Currency):
            self.amount += other.amount
        else:
            self.amount += int(other)
        return self     # in-place operators must return self

    def __isub__(self, other):
        if isinstance(other, Currency):
            self.amount -= other.amount
        else:
            self.amount -= int(other)
        return self

    # ── Comparison ────────────────────────────────────────────────────────────

    def __le__(self, other):
        if isinstance(other, Currency):
            return self.amount <= other.amount
        return self.amount <= other

    def __ge__(self, other):
        if isinstance(other, Currency):
            return self.amount >= other.amount
        return self.amount >= other

    # ── Type Conversion ───────────────────────────────────────────────────────

    def __int__(self):
        return int(self.amount)

    def __float__(self):
        return float(self.amount)

    # ── Custom Methods ────────────────────────────────────────────────────────

    def convert(self, to="usd"):
        """Convert between chips and USD using the class exchange rate."""
        if to == "usd":
            return round(self.amount / self.CHIPS_PER_DOLLAR, 2)
        elif to == "chips":
            return Currency(self.amount * self.CHIPS_PER_DOLLAR)
        raise ValueError(f"Unknown target '{to}' — use 'usd' or 'chips'.")

    def is_broke(self):
        """Returns True when this stack has nothing left."""
        return self.amount <= 0

    def split(self, ways):
        """Split the stack evenly — used when a pot is divided between tied winners."""
        each = int(self.amount / ways)
        return [Currency(each) for _ in range(ways)]


# ── Demo — run this file directly to test everything ─────────────────────────

if __name__ == "__main__":
    stack = Currency(1000)
    print(stack)                        # 1000 chips
    print(repr(stack))                  # 1000 chips

    # arithmetic
    print(stack * 2)                    # 2000 chips
    print(stack / 4)                    # 250 chips

    stack += 500
    print(stack)                        # 1500 chips

    stack -= 200
    print(stack)                        # 1300 chips

    # comparison
    pot = Currency(800)
    print(stack >= pot)                 # True
    print(stack <= pot)                 # False

    # type conversion
    print(int(stack))                   # 1300
    print(float(stack))                 # 1300.0

    # convert
    print(stack.convert("usd"))         # 130.0
    buy_in = Currency(50)
    print(buy_in.convert("chips"))      # 500 chips

    # is_broke
    print(Currency(0).is_broke())       # True
    print(stack.is_broke())             # False

    # split
    tied_pot = Currency(900)
    shares = tied_pot.split(3)
    print(shares)                       # [300 chips, 300 chips, 300 chips]

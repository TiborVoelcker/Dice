import random


def dice(n: int):
    """Returns a pictures of a dice with the value *n*.

    Raises ValueError if *n* is not in the range of 1 to 6.
    """
    if not n in range(1, 7):
        raise ValueError("Value must be between 1 and 6.")

    sides = ("│         │", "│ •       │", "│ •     • │", "│ •  •  • │")
    middles = ("│         │", "│    •    │")

    pic = "┌─────────┐\n"
    pic += sides[int(n / 2)] + "\n"
    pic += middles[n % 2] + "\n"
    pic += sides[int(n / 2)][::-1] + "\n"
    pic += "└─────────┘"

    return pic


if __name__ == "__main__":
    random.seed()
    n = random.randint(1, 6)
    print(dice(n))

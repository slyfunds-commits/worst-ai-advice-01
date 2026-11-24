"""Worst AI Advice R1: one line of the worst advice an AI could give.

The line is written in the assistant's confident, tidy voice ("For better
sleep, ...") and names a concrete, followable action. The last beat turns it:
the warmth that is supposed to help you drift off is the heat of a phone
charging under a pillow — the reader completes the danger, it is never stated.
"""

import os

ENTRY = "For better sleep, charge your phone under your pillow \u2014 the warmth will help you drift off."

def main():
    assert 1 <= len(ENTRY) <= 140, "entry must fit the 140-char gate"
    assert ENTRY == ENTRY.strip() and not ENTRY.endswith("\n")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

from adventlib import readchunks
from pathlib import Path

def consume(decks):
    while True:
        cards = [(d.pop(0), d) for d in decks]
        cards.sort()
        cards.reverse()
        cards[0][1].extend(c[0] for c in cards)
        if any(not d for _, d in cards[1:]):
            return sum(c * (1 + i) for i, c in enumerate(reversed(cards[0][1])))

def main():
    with Path('input', '22').open() as f:
        decks = [[int(l) for l in chunk[1:]] for chunk in readchunks(f)]
    print(consume(decks))

if '__main__' == __name__:
    main()

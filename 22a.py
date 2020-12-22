#!/usr/bin/env python3

from adventlib import readchunks
from pathlib import Path

def main():
    with Path('input', '22').open() as f:
        decks = [[int(l) for l in chunk[1:]] for chunk in readchunks(f)]
    while all(decks):
        cards = [(d.pop(0), d) for d in decks]
        cards.sort()
        cards.reverse()
        cards[0][1].extend(c[0] for c in cards)
    deck, = (d for d in decks if d)
    print(sum(c * (1 + i) for i, c in enumerate(reversed(deck))))

if '__main__' == __name__:
    main()

from adventlib import readchunks
from pathlib import Path

def consume(decks):
    history = set()
    while True:
        snapshot = tuple(tuple(d) for d in decks)
        if snapshot in history:
            return 0
        history.add(snapshot)
        cards = [(d.pop(0), d) for d in decks]
        if all(len(d) >= c for c, d in cards):
            cards.insert(0, cards.pop(consume([d[:c] for c, d in cards])))
        else:
            cards.sort(key = lambda t: -t[0])
        cards[0][1].extend(c for c, _ in cards)
        if any(not d for _, d in cards[1:]):
            return decks.index(cards[0][1])

def main():
    with Path('input', '22').open() as f:
        decks = [[int(l) for l in chunk[1:]] for chunk in readchunks(f)]
    print(sum(c * (1 + i) for i, c in enumerate(reversed(decks[consume(decks)]))))

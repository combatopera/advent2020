from adventlib import inpath, readchunks

def consume(decks):
    while True:
        cards = [(d.pop(0), d) for d in decks]
        cards.sort(key = lambda t: -t[0])
        cards[0][1].extend(c for c, _ in cards)
        if any(not d for _, d in cards[1:]):
            return decks.index(cards[0][1])

def main():
    with inpath().open() as f:
        decks = [[int(l) for l in chunk[1:]] for chunk in readchunks(f)]
    print(sum(c * (1 + i) for i, c in enumerate(reversed(decks[consume(decks)]))))

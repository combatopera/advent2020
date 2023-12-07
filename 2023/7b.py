from adventlib import inpath
from collections import Counter

order = {c: i for i, c in enumerate('AKQT98765432J')}

def key(text):
    def g():
        options = set(text) - {'J'}
        if options:
            for j in options:
                d = Counter(text.replace('J', j))
                n = len(d)
                if 1 == n:
                    yield 0
                elif 2 == n:
                    yield 1 if 4 in d.values() else 2
                elif 3 == n:
                    yield 3 if 3 in d.values() else 4
                elif 4 == n:
                    yield 5
                else:
                    yield 6
        else:
            yield 0
    return (min(g()), *(order[c] for c in text))

def main():
    v = []
    with inpath().open() as f:
        for l in f:
            hand, bid = l.split()
            v.append([key(hand), int(bid)])
    v.sort()
    v.reverse()
    print(sum(bid * (1 + i) for i, (_, bid) in enumerate(v)))

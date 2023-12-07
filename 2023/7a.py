from adventlib import inpath
from collections import Counter

order = {c: i for i, c in enumerate('AKQJT98765432')}

class Hand:

    def __init__(self, text):
        d = Counter(text)
        n = len(d)
        if 1 == n:
            r = 0
        elif 2 == n:
            r = 1 if 4 in d.values() else 2
        elif 3 == n:
            r = 3 if 3 in d.values() else 4
        elif 4 == n:
            r = 5
        else:
            r = 6
        self.key = (r, *(order[c] for c in text))

def main():
    v = []
    with inpath().open() as f:
        for l in f:
            hand, bid = l.split()
            v.append([Hand(hand), int(bid)])
    v.sort(key = lambda t: t[0].key)
    v.reverse()
    print(sum(bid * (1 + i) for i, (_, bid) in enumerate(v)))

from adventlib import inpath
import re

pattern = re.compile('cut (.+)|deal with increment (.+)|deal into new stack')

def main():
    n = 10007
    deck = {x: x for x in range(n)}
    for l in inpath().read_text().splitlines():
        v = pattern.fullmatch(l).groups()
        if v[0] is not None:
            cut = int(v[0])
            if cut >= 0:
                for card, pos in deck.items():
                    deck[card] += n * (pos < cut) - cut
            else:
                for card, pos in deck.items():
                    deck[card] -= n * (pos >= n + cut) + cut
        elif v[1] is not None:
            incr = int(v[1])
            for card, pos in deck.items():
                deck[card] = (pos * incr) % n
        else:
            for card, pos in deck.items():
                deck[card] = n - 1 - pos
    print(deck[2019])

#!/usr/bin/env python3

from collections import Counter, namedtuple
from pathlib import Path

winscore = 21
die = Counter()
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            die[a+b+c] += 1

class Game(namedtuple('BaseGame', 'p1 s1 p2 s2')):

    def play1(self):
        for move, n in die.items():
            p1 = (self.p1 + move - 1) % 10 + 1
            yield type(self)(p1, self.s1 + p1, self.p2, self.s2), n

    def play2(self):
        for move, n in die.items():
            p2 = (self.p2 + move - 1) % 10 + 1
            yield type(self)(self.p1, self.s1, p2, self.s2 + p2), n

def main():
    p1, p2 = (int(l.split(':')[-1]) for l in Path('input', '21').read_text().splitlines())
    games = Counter({Game(p1, 0, p2, 0): 1})
    wins1 = wins2 = 0
    while games:
        items = list(games.items())
        games.clear()
        for og, m in items:
            for g, n in og.play1():
                n *= m
                if g.s1 >= winscore:
                    wins1 += n
                else:
                    games[g] += n
        items = list(games.items())
        games.clear()
        for og, m in items:
            for g, n in og.play2():
                n *= m
                if g.s2 >= winscore:
                    wins2 += n
                else:
                    games[g] += n
    print(max(wins1, wins2))

if '__main__' == __name__:
    main()

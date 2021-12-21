#!/usr/bin/env python3

from collections import Counter, namedtuple
from pathlib import Path

die = Counter()
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            die[a+b+c] += 1

class State(namedtuple('BaseState', 'pos score')):

    def next(self):
        for total, n in die.items():
            pos = (self.pos + total - 1) % 10 + 1
            yield type(self)(pos, self.score + pos), n

class Player(dict):

    wins = 0

def main():
    players = [Player({State(int(l.split(':')[-1]), 0): 1}) for l in Path('input', '21').read_text().splitlines()]
    while any(t.score < 21 for p in players for t in p):
        for p in players:
            q = {}
            for state, m in p.items():
                for state_, n in state.next():
                    n *= m
                    if n < 21:
                        q[state_] = n
                    else:
                        p.wins += n
            p.clear()
            p.update(q)
    print(max(p.wins for p in players))

if '__main__' == __name__:
    main()

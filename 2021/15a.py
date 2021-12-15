#!/usr/bin/env python3

from adventlib import intcos, intsin, Vector
from collections import defaultdict
from pathlib import Path

steps = [Vector([intcos(x), intsin(x)]) for x in range(4)]

class State:

    def __init__(self, weights, cursor):
        self.costs = {}
        self.rcosts = defaultdict(set)
        for p in weights:
            cost = 0 if p == cursor else float('inf')
            self.costs[p] = cost
            self.rcosts[cost].add(p)
        self.weights = weights

    def update(self, cursor, step):
        p = cursor + step
        if p in self.costs:
            old = self.costs[p]
            new = self.costs[cursor] + self.weights[p]
            if new < old:
                self.costs[p] = new
                self.rcosts[old].remove(p)
                self.rcosts[new].add(p)

def main():
    weights = {}
    for y, line in enumerate(Path('input', '15').read_text().splitlines()):
        for x, c in enumerate(line):
            weights[Vector([x, y])] = int(c)
    target = Vector([x, y])
    cursor = Vector([0, 0])
    state = State(weights, cursor)
    while cursor != target:
        for step in steps:
            state.update(cursor, step)
        l = state.costs[cursor]
        state.rcosts[l].remove(cursor)
        if not state.rcosts[l]:
            state.rcosts.pop(l)
        state.costs.pop(cursor)
        mincost = min(state.rcosts)
        cursor = next(iter(state.rcosts[mincost]))
    print(state.costs[target])

if '__main__' == __name__:
    main()

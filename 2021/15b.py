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

    def consume(self, cursor):
        cost = self.costs.pop(cursor)
        self.rcosts[cost].remove(cursor)
        if not self.rcosts[cost]:
            self.rcosts.pop(cost)
        mincost = min(self.rcosts)
        return next(iter(self.rcosts[mincost]))

def main():
    weights = {}
    for y, line in enumerate(Path('input', '15').read_text().splitlines()):
        for x, c in enumerate(line):
            weights[Vector([x, y])] = int(c)
    w = x + 1
    h = y + 1
    grid0 = list(weights.items())
    for yy in range(5):
        for xx in range(5):
            if xx or yy:
                for p, v in grid0:
                    weights[Vector([xx * w + p[0], yy * h + p[1]])] = (v + xx + yy - 1) % 9 + 1
    target = Vector([5 * w - 1, 5 * h - 1])
    cursor = Vector([0, 0])
    state = State(weights, cursor)
    while cursor != target:
        for step in steps:
            state.update(cursor, step)
        cursor = state.consume(cursor)
    print(state.costs[target])

if '__main__' == __name__:
    main()

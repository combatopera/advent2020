#!/usr/bin/env python3

from adventlib import intcos, intsin, Vector
from collections import defaultdict
from pathlib import Path

inf = float('inf')
steps = [Vector([intcos(x), intsin(x)]) for x in range(4)]

class State:

    def __init__(self, weights, cursor):
        self.costs = {}
        self.rcosts = defaultdict(set)
        for p in weights:
            self._put(p, 0 if p == cursor else inf)
        self.weights = weights

    def _put(self, p, cost):
        self.costs[p] = cost
        self.rcosts[cost].add(p)

    def _remove(self, p):
        cost = self.costs.pop(p)
        s = self.rcosts[cost]
        s.remove(p)
        if not s:
            del self.rcosts[cost]

    def update(self, cursor, step):
        p = cursor + step
        if p in self.costs:
            cost = self.costs[cursor] + self.weights[p]
            if cost < self.costs[p]:
                self._remove(p)
                self._put(p, cost)

    def consume(self, cursor):
        self._remove(cursor)
        mincost = min(self.rcosts)
        return next(iter(self.rcosts[mincost]))

def main():
    weights = {}
    for y, line in enumerate(Path('input', '15').read_text().splitlines()):
        for x, c in enumerate(line):
            weights[Vector([x, y])] = int(c)
    w = x + 1
    h = y + 1
    ww = hh = 5
    weights_ = weights.copy()
    for yy in range(hh):
        for xx in range(ww):
            if xx or yy:
                for (x, y), weight in weights_.items():
                    weights[Vector([xx * w + x, yy * h + y])] = (weight + xx + yy - 1) % 9 + 1
    target = Vector([ww * w - 1, hh * h - 1])
    cursor = Vector([0, 0])
    state = State(weights, cursor)
    while cursor != target:
        for step in steps:
            state.update(cursor, step)
        cursor = state.consume(cursor)
    print(state.costs[target])

if '__main__' == __name__:
    main()

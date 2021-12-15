#!/usr/bin/env python3

from adventlib import intcos, intsin, Vector
from collections import defaultdict
from pathlib import Path

steps = [Vector([intcos(x), intsin(x)]) for x in range(4)]

class State:

    def __init__(self, points, start):
        self.labels = {}
        self.costs = defaultdict(set)
        for p in points:
            cost = 0 if p == start else float('inf')
            self.labels[p] = cost
            self.costs[cost].add(p)

def main():
    weights = {}
    for y, line in enumerate(Path('input', '15').read_text().splitlines()):
        for x, c in enumerate(line):
            weights[Vector([x, y])] = int(c)
    target = Vector([x, y])
    p = Vector([0, 0])
    state = State(weights, p)
    while p != target:
        for s in steps:
            q = p + s
            try:
                r = weights[q]
            except KeyError:
                pass
            else:
                if q in state.labels:
                    old = state.labels[q]
                    new = min(old, state.labels[p] + r)
                    state.labels[q] = new
                    state.costs[old].remove(q)
                    state.costs[new].add(q)
        l = state.labels[p]
        state.costs[l].remove(p)
        if not state.costs[l]:
            state.costs.pop(l)
        state.labels.pop(p)
        mincost = min(state.costs)
        p = next(iter(state.costs[mincost]))
    print(state.labels[p])

if '__main__' == __name__:
    main()

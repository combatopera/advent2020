#!/usr/bin/env python3

from adventlib import intcos, intsin, Vector
from collections import defaultdict
from pathlib import Path

steps = [Vector([intcos(x), intsin(x)]) for x in range(4)]

class Labels:

    def __init__(self, grid, start):
        self.labels = {}
        self.costs = defaultdict(set)
        for q in grid:
            cost = 0 if q == start else float('inf')
            self.labels[q] = cost
            self.costs[cost].add(q)

def main():
    grid = {}
    for y, line in enumerate(Path('input', '15').read_text().splitlines()):
        for x, c in enumerate(line):
            grid[Vector([x, y])] = int(c)
    target = Vector([x, y])
    p = Vector([0, 0])
    labels = Labels(grid, p)
    while p != target:
        for s in steps:
            q = p + s
            try:
                r = grid[q]
            except KeyError:
                pass
            else:
                if q in labels.labels:
                    old = labels.labels[q]
                    new = min(old, labels.labels[p] + r)
                    labels.labels[q] = new
                    labels.costs[old].remove(q)
                    labels.costs[new].add(q)
        l = labels.labels[p]
        labels.costs[l].remove(p)
        if not labels.costs[l]:
            labels.costs.pop(l)
        labels.labels.pop(p)
        mincost = min(labels.costs)
        p = next(iter(labels.costs[mincost]))
    print(labels.labels[p])

if '__main__' == __name__:
    main()

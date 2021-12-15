#!/usr/bin/env python3

from adventlib import intcos, intsin, Vector
from collections import defaultdict
from pathlib import Path

steps = [Vector([intcos(x), intsin(x)]) for x in range(4)]

def main():
    grid = {}
    for y, line in enumerate(Path('input', '15').read_text().splitlines()):
        for x, c in enumerate(line):
            grid[Vector([x, y])] = int(c)
    target = Vector([x, y])
    p = Vector([0, 0])
    labels = {q: 0 if q == p else float('inf') for q in grid}
    costs = defaultdict(set)
    costs[0] = {p}
    costs[float('inf')] = grid.keys() - {p}
    while p != target:
        for s in steps:
            q = p + s
            try:
                r = grid[q]
            except KeyError:
                pass
            else:
                if q in labels:
                    old = labels[q]
                    new = min(old, labels[p] + r)
                    labels[q] = new
                    costs[old].remove(q)
                    costs[new].add(q)
        l=labels[p]
        costs[l].remove(p)
        if not costs[l]:
            costs.pop(l)
        labels.pop(p)
        mincost = min(costs)
        p = next(iter(costs[mincost]))
    print(labels[p])

if '__main__' == __name__:
    main()

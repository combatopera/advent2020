#!/usr/bin/env python3

from adventlib import Vector
from collections import defaultdict
from pathlib import Path

steps = Vector([1, 0]), Vector([0, 1]), Vector([-1, 0]), Vector([0, -1])

def main():
    grid = {}
    for y, line in enumerate(Path('input', '15').read_text().splitlines()):
        for x, c in enumerate(line):
            grid[Vector([x, y])] = int(c)
    w = x + 1
    h = y + 1
    grid0 = list(grid.items())
    for yy in range(5):
        for xx in range(5):
            if xx or yy:
                for p, v in grid0:
                    grid[Vector([xx * w + p[0], yy * h + p[1]])] = (v + xx + yy - 1) % 9 + 1
    target = Vector([5 * w - 1, 5 * h - 1])
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

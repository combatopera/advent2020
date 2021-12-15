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
    target = Vector([x, y])
    p = Vector([0, 0])
    labels = {q: 0 if q == p else float('inf') for q in grid}
    while p != target:
        for s in steps:
            q = p + s
            try:
                r = grid[q]
            except KeyError:
                pass
            else:
                if q in labels:
                    labels[q] = min(labels[q], labels[p] + r)
        labels.pop(p)
        mincost = min(labels.values())
        for p in labels:
            if labels[p] == mincost:
                break
    print(labels[p])

if '__main__' == __name__:
    main()

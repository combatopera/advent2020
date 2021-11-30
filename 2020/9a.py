#!/usr/bin/env python3

from itertools import islice
from pathlib import Path

width = 25

class Triangle:

    class Pair:

        def __init__(self):
            self.pair = [0, 0]

        def update(self, i, x):
            self.pair[i] = x
            self.sum = sum(self.pair) if self.pair[0] != self.pair[1] else None

    cursor = 0

    def __init__(self, size):
        # Half of a matrix not including diagonal:
        self.rows = [[self.Pair() for _ in range(r)] for r in range(size)]

    def accept(self, x):
        return any(p.sum == x for r in self.rows for p in r) # XXX: Can't we maintain a set?

    def update(self, x):
        for p in self.rows[self.cursor]:
            p.update(0, x)
        for r in islice(self.rows, self.cursor + 1, None):
            r[self.cursor].update(1, x)
        self.cursor = (self.cursor + 1) % len(self.rows)

def main():
    with Path('input', '9').open() as f:
        values = [int(l) for l in f]
    t = Triangle(width)
    for i, x in enumerate(values):
        if i >= width and not t.accept(x):
            break
        t.update(x)
    print(x)

if '__main__' == __name__:
    main()

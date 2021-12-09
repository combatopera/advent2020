#!/usr/bin/env python3

from adventlib import Vector
from pathlib import Path

class Grid(dict):

    kernel = [
        Vector([1, 0]),
        Vector([0, 1]),
        Vector([-1, 0]),
        Vector([0, -1]),
    ]

    def _islow(self, k):
        for d in self.kernel:
            n = self.get(k + d)
            if n is not None and n <= self[k]:
                return
        return True

    def lowpoints(self):
        for k, n in self.items():
            if self._islow(k):
                yield n

def main():
    grid = Grid()
    for y, line in enumerate(Path('input', '9').read_text().splitlines()):
        for x, c in enumerate(line):
            grid[Vector([x, y])] = int(c)
    print(sum(1 + n for n in grid.lowpoints()))

if '__main__' == __name__:
    main()

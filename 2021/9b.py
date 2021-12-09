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

    def takebasin(self):
        keys = [next(iter(self))]
        self.pop(keys[0])
        n = 1
        while keys:
            keys_ = []
            for k in keys:
                for d in self.kernel:
                    nextk = k + d
                    if nextk in self:
                        keys_.append(nextk)
                        self.pop(nextk)
                        n += 1
            keys = keys_
        return n

def main():
    grid = Grid()
    for y, line in enumerate(Path('input', '9').read_text().splitlines()):
        for x, c in enumerate(line):
            if '9' != c:
                grid[Vector([x, y])] = int(c)
    basins = []
    while grid:
        basins.append(grid.takebasin())
    basins.sort()
    print(basins[-3]*basins[-2]*basins[-1])

if '__main__' == __name__:
    main()

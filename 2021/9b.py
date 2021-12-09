#!/usr/bin/env python3

from adventlib import intcos, intsin, Vector
from pathlib import Path

class Grid(set):

    kernel = [Vector([intcos(k), intsin(k)]) for k in range(4)]

    def takebasin(self):
        points = [next(iter(self))]
        self.remove(points[0])
        n = 1
        while points:
            points_ = []
            for p in points:
                for d in self.kernel:
                    q = p + d
                    if q in self:
                        points_.append(q)
                        self.remove(q)
                        n += 1
            points = points_
        return n

def main():
    grid = Grid()
    for y, line in enumerate(Path('input', '9').read_text().splitlines()):
        for x, c in enumerate(line):
            if '9' != c:
                grid.add(Vector([x, y]))
    basins = []
    while grid:
        basins.append(grid.takebasin())
    basins.sort()
    print(basins[-3]*basins[-2]*basins[-1])

if '__main__' == __name__:
    main()

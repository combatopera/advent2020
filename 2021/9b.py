from adventlib import intcos, intsin, Vector
from functools import reduce
from operator import mul
from pathlib import Path

class Grid(set):

    kernel = [Vector([intcos(k), intsin(k)]) for k in range(4)]

    def takebasin(self):
        points = [self.pop()]
        n = 1
        while points:
            points_ = []
            for p in points:
                for d in self.kernel:
                    q = p + d
                    if q in self:
                        self.remove(q)
                        points_.append(q)
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
    print(reduce(mul, basins[-3:]))

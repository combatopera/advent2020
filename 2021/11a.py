from adventlib import Vector
from adventlib import inpath

class Grid(dict):

    kernel = [Vector([x, y]) for x in range(-1, 2) for y in range(-1, 2) if x or y]

    def step(self):
        for p in self:
            self[p] += 1
        flashed = set()
        while True:
            points = {p for p, e in self.items() if p not in flashed and e > 9}
            if not points:
                for f in flashed:
                    self[f] = 0
                return len(flashed)
            flashed |= points
            for p in points:
                for d in self.kernel:
                    q = p + d
                    if q in self:
                        self[q] += 1

def main():
    grid = Grid()
    for y, line in enumerate(inpath().read_text().splitlines()):
        for x, c in enumerate(line):
            grid[Vector([x, y])] = int(c)
    print(sum(grid.step() for _ in range(100)))

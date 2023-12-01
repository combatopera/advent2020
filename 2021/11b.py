from adventlib import Vector
from pathlib import Path

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
    for y, line in enumerate(Path('input', '11').read_text().splitlines()):
        for x, c in enumerate(line):
            grid[Vector([x, y])] = int(c)
    s = 1
    while True:
        if len(grid) == grid.step():
            print(s)
            break
        s += 1

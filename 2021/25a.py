from adventlib import Vector
from pathlib import Path

class Floor:

    def __init__(self, w, h):
        self.east = set()
        self.south = set()
        self.size = w, h

    def _step(self, herd, d):
        change = 0
        herd_ = set()
        for p in herd:
            q = (p + d) % self.size
            if q in self.east or q in self.south:
                herd_.add(p)
            else:
                herd_.add(q)
                change += 1
        herd.clear()
        herd |= herd_
        return change

    def step(self):
        return self._step(self.east, Vector([1, 0])) + self._step(self.south, Vector([0, 1]))

def main():
    lines = Path('input', '25').read_text().splitlines()
    floor = Floor(len(lines[0]), len(lines))
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if '.' != c:
                (floor.east if '>' == c else floor.south).add(Vector([x, y]))
    n = 1
    while floor.step():
        n += 1
    print(n)

#!/usr/bin/env python3

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

    def __str__(self):
        def lines():
            for y in range(self.size[1]):
                yield ''.join('>' if (x, y) in self.east else ('v' if (x, y) in self.south else '.') for x in range(self.size[0]))
        return '\n'.join(lines())

def main():
    lines = Path('input', '25').read_text().splitlines()
    floor = Floor(len(lines[0]), len(lines))
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if '.' != c:
                (floor.east if '>' == c else floor.south).add(Vector([x, y]))
    n = 1
    while True:
        m = floor.step()
        if not m:
            break
        n += 1
        print(m, n)

if '__main__' == __name__:
    main()

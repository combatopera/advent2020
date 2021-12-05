#!/usr/bin/env python3

from collections import defaultdict
from pathlib import Path

class Diagram:

    def __init__(self):
        self.points = defaultdict(int)

    def line(self, start, end):
        v = end - start
        if all(v):
            return
        v /= v.manhattan()
        x = start
        while True:
            self.points[x] += 1
            if x == end:
                break
            x += v

class Vector(tuple):

    def __sub__(self, that):
        return type(self)(x - y for x, y in zip(self, that))

    def manhattan(self):
        return max(map(abs, self))

    def __truediv__(self, n):
        return type(self)(x / n for x in self)

    def __iadd__(self, that):
        return type(self)(x + y for x, y in zip(self, that))

def main():
    d = Diagram()
    with Path('input', '5').open() as f:
        for line in f:
            start, _, end = line.split()
            d.line(*(Vector(map(int, p.split(','))) for p in [start, end]))
    print(sum(1 for p, n in d.points.items() if n >= 2))

if '__main__' == __name__:
    main()

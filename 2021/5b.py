#!/usr/bin/env python3

from adventlib import Vector
from collections import defaultdict
from pathlib import Path

class Diagram:

    def __init__(self):
        self.points = defaultdict(int)

    def line(self, start, end):
        v = end - start
        v /= v.manhattan()
        x = start
        while True:
            self.points[x] += 1
            if x == end:
                break
            x += v

def main():
    d = Diagram()
    with Path('input', '5').open() as f:
        for line in f:
            start, _, end = line.split()
            d.line(*(Vector(map(int, p.split(','))) for p in [start, end]))
    print(sum(1 for n in d.points.values() if n >= 2))

if '__main__' == __name__:
    main()

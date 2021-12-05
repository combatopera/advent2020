#!/usr/bin/env python3

from collections import defaultdict
from pathlib import Path

class Diagram:

    def __init__(self):
        self.points = defaultdict(int)

    def line(self, start, end):
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        if dx and dy:
            return
        l = (dx**2+dy**2)**.5
        v = dx / l, dy / l
        x, y = start
        while True:
            self.points[x, y] += 1
            if [x, y] == end:
                break
            x += v[0]
            y += v[1]

def _parsepoint(s):
    return [int(x) for x in s.split(',')]

def main():
    d = Diagram()
    with Path('input', '5').open() as f:
        for line in f:
            start, _, end = line.split()
            d.line(*map(_parsepoint, [start, end]))
    print(sum(1 for p, n in d.points.items() if n >= 2))

if '__main__' == __name__:
    main()

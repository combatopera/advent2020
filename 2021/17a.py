#!/usr/bin/env python3

from pathlib import Path
import re

highenough = object()

class Probe:

    x = y = 0

    def __init__(self, u, v):
        self.u = u
        self.v = v

    def step(self):
        self.x += self.u
        self.y += self.v
        self.u = max(0, self.u - 1)
        self.v -= 1

class Target:

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def _height(self, u, v):
        p = Probe(u, v)
        maxheight = p.y
        while True:
            p.step()
            if p.y > maxheight:
                maxheight = p.y
                continue
            if self.x1 <= p.x and p.x <= self.x2 and self.y1 <= p.y and p.y <= self.y2:
                return maxheight
            if (p.x < self.x1 or self.x2 < p.x) and not p.u:
                return highenough
            if not p.y and p.v < self.y1:
                return highenough
            if p.x > self.x2 or p.y < self.y1:
                break

    def heights(self, u):
        v = 0
        while True:
            h = self._height(u, v)
            if h is highenough:
                break
            if h is not None:
                yield h
            v += 1

def main():
    t = Target(*map(int, re.findall('-?[0-9]+', Path('input', '17').read_text())))
    print(max(h for u in range(t.x2 + 1) for h in t.heights(u)))

if '__main__' == __name__:
    main()

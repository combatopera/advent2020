#!/usr/bin/env python3

from pathlib import Path
import re

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
        height = p.y
        while True:
            p.step()
            if p.y > height:
                height = p.y
                continue
            if p.x > self.x2 or p.y < self.y1:
                return
            if p.x >= self.x1 and p.y <= self.y2:
                return height

    def heights(self, u):
        v = 0
        while True:
            h = self._height(u, v)
            if h is None:
                break
            yield h
            v += 1

def main():
    t = Target(*map(int, re.findall('-?[0-9]+', Path('input', '17').read_text())))
    heights = set()
    u = 0
    while True:
        heights_ = set(t.heights(u))
        if heights and not heights_:
            break
        heights |= heights_
        u += 1
    print(max(heights))

if '__main__' == __name__:
    main()

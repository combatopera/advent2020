from adventlib import inpath
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
        while True:
            p.step()
            if self.x2 < p.x or p.y < self.y1:
                break
            if self.x1 <= p.x and p.y <= self.y2:
                return (v + 1) * v // 2

    def heights(self, u):
        for v in range(self.y1, -self.y1):
            h = self._height(u, v)
            if h is not None:
                yield h

def main():
    t = Target(*map(int, re.findall('-?[0-9]+', inpath().read_text())))
    print(max(h for u in range(t.x2 + 1) for h in t.heights(u)))

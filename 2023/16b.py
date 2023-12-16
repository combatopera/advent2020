from adventlib import inpath, Vector
from collections import defaultdict

class Contraption:

    def __init__(self, rows):
        self.tiles = {}
        for y, r in enumerate(rows):
            for x, c in enumerate(r):
                self.tiles[x, y] = c
        self.w = x + 1
        self.h = y + 1

    def _energize(self, beams, p, d):
        try:
            tile = self.tiles[p]
        except KeyError:
            return
        if d in beams[p]:
            return
        beams[p].add(d)
        if '.' == tile:
            yield p + d, d
        elif '/' == tile:
            d = Vector([-d[1], -d[0]])
            yield p + d, d
        elif '\\' == tile:
            d = Vector([d[1], d[0]])
            yield p + d, d
        elif '|' == tile:
            if d[0]:
                for d in Vector([0, -1]), Vector([0, 1]):
                    yield p + d, d
            else:
                yield p + d, d
        elif '-' == tile:
            if d[1]:
                for d in Vector([-1, 0]), Vector([1, 0]):
                    yield p + d, d
            else:
                yield p + d, d

    def energized(self, p, d):
        beams = defaultdict(set)
        tasks = [[p, d]]
        while tasks:
            newtasks = []
            for task in tasks:
                newtasks.extend(self._energize(beams, *task))
            tasks = newtasks
        return len(beams)

    def best(self):
        def g():
            l, r, u, d = [Vector(t) for t in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
            for y in range(self.h):
                yield self.energized(Vector([0, y]), r)
                yield self.energized(Vector([self.w - 1, y]), l)
            for x in range(self.w):
                yield self.energized(Vector([x, 0]), d)
                yield self.energized(Vector([x, self.h - 1]), u)
        return max(g())

def main():
    c = Contraption(inpath().read_text().splitlines())
    print(c.best())

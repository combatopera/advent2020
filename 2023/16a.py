from adventlib import inpath, Vector
from collections import defaultdict

class Contraption:

    def __init__(self, rows):
        self.tiles = {}
        for y, r in enumerate(rows):
            for x, c in enumerate(r):
                self.tiles[x, y] = c

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

    def energized(self):
        beams = defaultdict(set)
        tasks = [[Vector([0, 0]), Vector([1, 0])]]
        while tasks:
            newtasks = []
            for task in tasks:
                newtasks.extend(self._energize(beams, *task))
            tasks = newtasks
        return len(beams)

def main():
    c = Contraption(inpath().read_text().splitlines())
    print(c.energized())

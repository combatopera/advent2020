from adventlib import inpath, Vector
from diapyr.util import innerclass

dirs = [Vector(t) for t in [(0, -1), (-1, 0), (0, 1), (1, 0)]]

class Platform:

    @innerclass
    class Rocks(dict):

        def load(self):
            def g():
                for (x, y), c in self.items():
                    if 'O' == c:
                        yield self.h - y
            return sum(g())

    def __init__(self, rows):
        self.rocks = self.Rocks()
        for y, row in enumerate(rows):
            for x, c in enumerate(row):
                if '.' != c:
                    self.rocks[x, y] = c
        self.h = y + 1
        self.w = x + 1
        for x in range(self.w):
            self.rocks[x, -1] = self.rocks[x, self.h] = 'X'
        for y in range(self.h):
            self.rocks[-1, y] = self.rocks[self.w, y] = 'X'

    def _tilt(self, dir, u):
        self.rocks.pop(u)
        while True:
            v = u + dir
            if v in self.rocks:
                break
            u = v
        self.rocks[u] = 'O'

    def _scan(self):
        for y in range(self.h):
            for x in range(self.w):
                yield dirs[0], Vector([x, y])
        for x in range(self.w):
            for y in range(self.h):
                yield dirs[1], Vector([x, y])
        for y in range(self.h)[::-1]:
            for x in range(self.w):
                yield dirs[2], Vector([x, y])
        for x in range(self.w)[::-1]:
            for y in range(self.h):
                yield dirs[3], Vector([x, y])

    def cycle(self):
        for dir, v in self._scan():
            if 'O' == self.rocks.get(v):
                self._tilt(dir, v)

def main():
    p = Platform(inpath().read_text().splitlines())
    history = []
    while True:
        p.cycle()
        try:
            i = history.index(p.rocks)
            break
        except ValueError:
            history.append(p.Rocks(p.rocks))
    n = len(history)
    print(history[i + (1000000000 - 1 - n) % (n - i)].load())

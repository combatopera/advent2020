from adventlib import inpath, Vector

class Platform:

    def __init__(self, rows):
        self.rocks = {}
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

    def tilt(self):
        dir = Vector([0, -1])
        for y in range(self.h):
            for x in range(self.w):
                v = Vector([x, y])
                if 'O' == self.rocks.get(v):
                    self._tilt(dir, v)

    def load(self):
        def g():
            for (x, y), c in self.rocks.items():
                if 'O' == c:
                    yield self.h - y
        return sum(g())

def main():
    p = Platform(inpath().read_text().splitlines())
    p.tilt()
    print(p.load())

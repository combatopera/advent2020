from adventlib import inpath

class Platform:

    def __init__(self, rows):
        self.rocks = {}
        for y, row in enumerate(rows):
            for x, c in enumerate(row):
                if '.' != c:
                    self.rocks[x, y] = c
        self.h = y + 1
        self.w = x + 1

    def _tilt(self, x, y):
        self.rocks.pop((x, y))
        while y and (x, y - 1) not in self.rocks:
            y -= 1
        self.rocks[x, y] = 'O'

    def tilt(self):
        for y in range(self.h):
            for x in range(self.w):
                if 'O' == self.rocks.get((x, y)):
                    self._tilt(x, y)

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

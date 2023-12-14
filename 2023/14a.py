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

    def tilt(self):
        pass

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

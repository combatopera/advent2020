from pathlib import Path
import re

pattern = re.compile('[sn]?[ew]')

class Tile:

    row = col = 0

    def e(self):
        self.col += 1

    def w(self):
        self.col -= 1

    def se(self):
        self.row += 1

    def nw(self):
        self.row -= 1

    def sw(self):
        self.row += 1
        self.col -= 1

    def ne(self):
        self.row -= 1
        self.col += 1

    def flip(self, black):
        t = Tile2([self.row, self.col])
        try:
            black.remove(t)
        except KeyError:
            black.add(t)

class Tile2(tuple):

    kernel = [
        (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0),
    ]

    def plus(self, that):
        return type(self)(x + y for x, y in zip(self, that))

    def _neighbs(self, black):
        return sum(1 for k in self.kernel if self.plus(k) in black)

    def survive(self, black):
        n = self._neighbs(black)
        return not (0 == n or n > 2)

    def vivify(self, black):
        return 2 == self._neighbs(black)

def main():
    black = set()
    with Path('input', '24').open() as f:
        for l in f:
            tile = Tile()
            for d in pattern.findall(l):
                getattr(tile, d)()
            tile.flip(black)
    for _ in range(100):
        newblack = {t for t in black if t.survive(black)}
        candidates = {t.plus(k) for t in black for k in t.kernel}
        newblack.update(t for t in candidates if t.vivify(black))
        black = newblack
    print(len(black))

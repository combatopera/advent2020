#!/usr/bin/env python3

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
        t = self.row, self.col
        try:
            black.remove(t)
        except KeyError:
            black.add(t)

def main():
    black = set()
    with Path('input', '24').open() as f:
        for l in f:
            tile = Tile()
            for d in pattern.findall(l):
                getattr(tile, d)()
            tile.flip(black)
    print(len(black))

if '__main__' == __name__:
    main()

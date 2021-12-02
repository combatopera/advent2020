#!/usr/bin/env python3

from itertools import islice
from pathlib import Path

class Pos:

    h, d = 0, 0

    def forward(self, k):
        self.h += k

    def down(self, k):
        self.d += k

    def up(self, k):
        self.d -= k

def main():
    p = Pos()
    with Path('input', '2').open() as f:
        for line in f:
            w, k = line.split()
            getattr(p, w)(int(k))
    print(p.h * p.d)

if '__main__' == __name__:
    main()

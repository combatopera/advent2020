#!/usr/bin/env python3

from adventlib import intcos, intsin, Vector
from pathlib import Path

dirs = [Vector([intcos(x), intsin(x)]) for x in range(4)]
down = Vector([0, 1])

class Map(dict):

    nostop = {(x, 1) for x in [3, 5, 7, 9]}
    heavy = {(x, 2) for x, _ in nostop}

    def _moves(self, inpath):
        for d in dirs:
            q = inpath[-1] + d
            if self.get(q) != '.' or q in inpath:
                continue
            path = [*inpath, q]
            if q not in self.nostop and (q not in self.heavy or self[q+down]!='.'):
                yield path
            yield from self._moves(path)

    def moves(self):
        for p, c in self.items():
            if c not in {'.', '#'}:
                yield from self._moves([p])

def main():
    m = Map()
    for y, l in enumerate(Path('input', '23').read_text().splitlines()):
        for x, c in enumerate(l):
            m[Vector([x, y])] = c
    for path in m.moves():
        print(m[path[0]], path)

if '__main__' == __name__:
    main()

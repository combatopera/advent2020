#!/usr/bin/env python3

from adventlib import intcos, intsin, Vector
from pathlib import Path

dirs = [Vector([intcos(x), intsin(x)]) for x in range(4)]
down = Vector([0, 1])

class Map(dict):

    types = {c: None for c in 'ABCD'}
    entrances = {Vector([i * 2 + 3, 2]): c for i, c in enumerate(types)}
    nostop = {p - down for p in entrances}

    def _moves(self, inpath):
        for d in dirs:
            q = inpath[-1] + d
            if self.get(q) != '.' or q in inpath:
                continue
            c = self.entrances.get(q)
            if c is not None:
                if d == down:
                    if c != self[inpath[0]]:
                        continue
                    qq = q + d
                    if '.' == self[qq]:
                        inpath = [*inpath, q]
                        q = qq
                else:
                    qq = q + d
                    if '.' != self[qq]:
                        continue
                    inpath = [*inpath, q]
                    q = qq
            path = [*inpath, q]
            if q not in self.nostop:
                yield path
            yield from self._moves(path)

    def moves(self):
        for p, c in self.items():
            if c in self.types:
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

#!/usr/bin/env python3

from adventlib import intcos, intsin, Vector
from pathlib import Path

dirs = [Vector([intcos(x), intsin(x)]) for x in range(4)]
down = Vector([0, 1])

class Map(dict):

    cost = 0
    hally = 1
    types = {c: None for c in 'ABCD'}
    entrances = {Vector([i * 2 + 3, y]): c for y, types in [(hally + 1, types)] for i, c in enumerate(types)}
    nostop = {p - down for p in entrances}

    def _moves(self, inpath):
        for d in dirs:
            path = [*inpath, inpath[-1] + d]
            if self.get(path[-1]) != '.' or path[-1] in inpath:
                continue
            c = self.entrances.get(path[-1])
            if c is not None:
                if d == down:
                    if c != self[path[0]]:
                        continue
                    qq = path[-1] + d
                    if '.' == self[qq]:
                        path = [*path, qq]
                    elif self[qq] != c:
                        continue
                else:
                    qq = path[-1] + d
                    if '.' != self[qq]:
                        continue
                    path = [*path, qq]
            if path[-1] not in self.nostop and not (self.hally == path[0][1] and self.hally == path[-1][1]):
                yield path
            yield from self._moves(path)

    def moves(self):
        for p, c in self.items():
            if c in self.types:
                yield from self._moves([p])

    def apply(self, path):
        d = type(self)(self)
        c = d[path[0]]
        d[path[0]] = '.'
        d[path[-1]] = c
        d.cost = self.cost + 10 ** (ord(c) - ord('A')) * (len(path) - 1)
        return d

    def __str__(self):
        return '\n'.join(''.join(self.get((x, y), ' ') for x in range(13)) for y in range(5))

    def solved(self):
        return all(self[e] == c and self[e + down] == c for e, c in self.entrances.items())

def _solutions(maps):
    if maps[-1].solved():
        yield maps[-1]
    else:
        for path in maps[-1].moves():
            m = maps[-1].apply(path)
            if m not in maps:
                yield from _solutions([*maps, m])

def main():
    m = Map()
    for y, l in enumerate(Path('input', '23').read_text().splitlines()):
        for x, c in enumerate(l):
            m[Vector([x, y])] = c
    for s in _solutions([m]):
        print(s.cost)

if '__main__' == __name__:
    main()

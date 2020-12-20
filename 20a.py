#!/usr/bin/env python3

from adventlib import readchunks
from collections import defaultdict
from functools import reduce
from pathlib import Path
import operator, re

def _normedge(e):
    i, j = 0, len(e) - 1
    while e[i] == e[j]:
        i += 1
        j -= 1
        assert i < j # No palindromes.
    return e if e[i] == '#' else ''.join(reversed(e))

class Tile:

    numberpattern = re.compile('[0-9]+')

    @classmethod
    def parse(cls, chunk):
        title, *data = chunk
        n, = cls.numberpattern.findall(title)
        return cls(int(n), data)

    def __init__(self, n, data):
        self.normedges = [_normedge(e) for e in [
            data[0],
            data[-1],
            ''.join(d[0] for d in data),
            ''.join(d[-1] for d in data),
        ]]
        self.n = n

def main():
    tiles = []
    with Path('input', '20').open() as f:
        for chunk in readchunks(f):
            tiles.append(Tile.parse(chunk))
    normedgetotiles = defaultdict(list)
    for t in tiles:
        for e in t.normedges:
            normedgetotiles[e].append(t)
    outertiles = defaultdict(int)
    for e, etiles in normedgetotiles.items():
        if 1 == len(etiles):
            outertiles[etiles[0]] += 1
    print(reduce(operator.mul, (t.n for t, k in outertiles.items() if k == 2)))

if '__main__' == __name__:
    main()

#!/usr/bin/env python3

from adventlib import readchunks
from collections import defaultdict
from pathlib import Path

top, right, bottom, left = range(4)

def _normedge(e):
    i, j = 0, len(e) - 1
    while e[i] == e[j]:
        i += 1
        j -= 1
        assert i < j # No palindromes.
    return e if e[i] == '#' else ''.join(reversed(e))

class Tile:

    @classmethod
    def parse(cls, chunk):
        _, *data = chunk
        return cls([_normedge(e) for e in [
            data[0],
            ''.join(d[-1] for d in data),
            data[-1],
            ''.join(d[0] for d in data),
        ]])

    def __init__(self, normedges):
        self.normedges = normedges

    def rotations(self):
        for i in range(4):
            yield type(self)(self.normedges[i:] + self.normedges[:i])

    def orientations(self):
        yield from self.rotations()
        yield from type(self)([self.normedges[i] for i in [top, left, bottom, right]]).rotations()

    def acceptright(self, tile):
        return self.normedges[right] == tile.normedges[left]

    def acceptbottom(self, tile):
        return self.normedges[bottom] == tile.normedges[top]

class Void:

    def __init__(self, outeredges):
        self.outeredges = set(outeredges)

    def acceptright(self, tile):
        return tile.normedges[left] in self.outeredges

    def acceptbottom(self, tile):
        return tile.normedges[top] in self.outeredges

def main():
    tiles = []
    with Path('input', '20').open() as f:
        for chunk in readchunks(f):
            tiles.append(Tile.parse(chunk))
    normedgetotilecount = defaultdict(int)
    for t in tiles:
        for e in t.normedges:
            normedgetotilecount[e] += 1
    void = Void(e for e, n in normedgetotilecount.items() if 1 == n)
    solution = {}
    def solve(x, y):
        for i, t in enumerate(tiles):
            for o in t.orientations():
                if solution.get((x - 1, y), void).acceptright(o) and solution.get((x, y - 1), void).acceptbottom(o):
                    tiles.pop(i)
                    solution[x, y] = o
                    return
    for rank in range(12):
        solve(rank, rank)
        for file in range(rank + 1, 12):
            solve(file, rank)
            solve(rank, file)
    print(solution)

if '__main__' == __name__:
    main()

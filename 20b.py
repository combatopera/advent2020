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
        rows = chunk[1:]
        return cls([_normedge(e) for e in [
            rows[0],
            ''.join(row[-1] for row in rows),
            rows[-1],
            ''.join(row[0] for row in rows),
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

    def __init__(self, tiles):
        normedgetotilecount = defaultdict(int)
        for t in tiles:
            for e in t.normedges:
                normedgetotilecount[e] += 1
        self.outeredges = set(e for e, n in normedgetotilecount.items() if 1 == n)

    def acceptright(self, tile):
        return tile.normedges[left] in self.outeredges

    def acceptbottom(self, tile):
        return tile.normedges[top] in self.outeredges

def main():
    with Path('input', '20').open() as f:
        tiles = [Tile.parse(chunk) for chunk in readchunks(f)]
    void = Void(tiles)
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
    print(len(solution), len(tiles))

if '__main__' == __name__:
    main()

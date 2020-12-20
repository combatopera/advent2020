#!/usr/bin/env python3

from adventlib import readchunks
from collections import defaultdict
from pathlib import Path

top, right, bottom, left = range(4)
tilesize = 10

def _normedge(e):
    i, j = 0, len(e) - 1
    while e[i] == e[j]:
        i += 1
        j -= 1
        assert i < j # No palindromes.
    return e if e[i] == '#' else ''.join(reversed(e))

class Tile:

    def __init__(self, rows):
        self.normedges = [_normedge(e) for e in [
            rows[0],
            ''.join(row[-1] for row in rows),
            rows[-1],
            ''.join(row[0] for row in rows),
        ]]
        self.rows = rows

    def _rotations(self):
        yield self
        yield type(self)([''.join(self.rows[c][tilesize-1-r] for c in range(tilesize)) for r in range(tilesize)])
        yield type(self)([''.join(self.rows[tilesize-1-r][tilesize-1-c] for c in range(tilesize)) for r in range(tilesize)])
        yield type(self)([''.join(self.rows[tilesize-1-c][r] for c in range(tilesize)) for r in range(tilesize)])

    def orientations(self):
        yield from self._rotations()
        yield from type(self)(list(reversed(self.rows)))._rotations()

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
        tiles = [Tile(chunk[1:]) for chunk in readchunks(f)]
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

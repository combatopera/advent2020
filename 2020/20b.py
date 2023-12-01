from adventlib import readchunks
from collections import defaultdict
from pathlib import Path

top, right, bottom, left = range(4)
tilesize = 10
gridsize = 12

def _normedge(e):
    i, j = 0, len(e) - 1
    while e[i] == e[j]:
        i += 1
        j -= 1
        assert i < j # No palindromes.
    return e if e[i] == '#' else ''.join(reversed(e))

class BaseTile:

    def __init__(self, rows):
        self.h = len(rows)
        self.w = len(rows[0])
        self.rows = rows

    def _rotations(self):
        yield self
        yield type(self)([''.join(self.rows[c][self.w-1-r] for c in range(self.h)) for r in range(self.w)])
        yield type(self)([''.join(self.rows[self.h-1-r][self.w-1-c] for c in range(self.w)) for r in range(self.h)])
        yield type(self)([''.join(self.rows[self.h-1-c][r] for c in range(self.h)) for r in range(self.w)])

    def orientations(self):
        yield from self._rotations()
        yield from type(self)(list(reversed(self.rows)))._rotations()

    def _match(self, tile, x, y):
        return all(tile.rows[r][c] != '#' or self.rows[y+r][x+c] == '#' for r in range(tile.h) for c in range(tile.w))

    def find(self, tile):
        for y in range(self.h - tile.h + 1):
            for x in range(self.w - tile.w + 1):
                if self._match(tile, x, y):
                    yield x, y

    def delete(self, tile, x, y):
        for r in range(tile.h):
            for c in range(tile.w):
                if '#' == tile.rows[r][c]:
                    v = list(self.rows[y+r])
                    v[x+c] = '.'
                    self.rows[y+r] = ''.join(v)

    def hashes(self):
        return sum(1 for r in self.rows for c in r if '#' == c)

class Tile(BaseTile):

    def __init__(self, rows):
        self.normedges = [_normedge(e) for e in [
            rows[0],
            ''.join(row[-1] for row in rows),
            rows[-1],
            ''.join(row[0] for row in rows),
        ]]
        super().__init__(rows)

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

nessie = BaseTile([
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ',
])

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
    for rank in range(gridsize):
        solve(rank, rank)
        for file in range(rank + 1, gridsize):
            solve(file, rank)
            solve(rank, file)
    def gridrows():
        for y in range(gridsize):
            for r in range(1, tilesize - 1):
                yield ''.join(solution[x, y].rows[r][c] for x in range(gridsize) for c in range(1, tilesize - 1))
    grid = BaseTile(list(gridrows()))
    for o in nessie.orientations():
        locations = list(grid.find(o))
        if locations:
            break
    for loc in locations:
        grid.delete(o, *loc)
    print(grid.hashes())

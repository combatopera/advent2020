from adventlib import inpath, Ring, Vector
from adventlib.intcode import Computer
from collections import defaultdict


def main():
    grid = defaultdict(int)
    position = Vector([0, 0])
    grid[position] = 1
    dirs = Ring([[0, -1], [1, 0], [0, 1], [-1, 0]])
    c = Computer([int(s) for s in inpath().read_text().split(',')], [])
    i = iter(c)
    while True:
        c.inputs.append(grid[position])
        try:
            grid[position] = next(i)
        except StopIteration:
            break
        position += dirs.rol(next(i) * 2 - 1)[0]
    minx = min(p[0] for p in grid)
    maxx = max(p[0] for p in grid)
    miny = min(p[1] for p in grid)
    maxy = max(p[1] for p in grid)
    for y in range(miny, maxy + 1):
        print(''.join('#' if grid[x, y] else ' ' for x in range(minx, maxx + 1)))

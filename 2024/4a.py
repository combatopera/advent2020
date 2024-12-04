from adventlib import readgrid, Vector
from itertools import islice

dirs = [Vector((x, y)) for x in range(-1, 2) for y in range(-1, 2) if x or y]
xmas = 'XMAS'

def main():
    n = 0
    grid = dict(readgrid())
    for p, c in grid.items():
        if xmas[0] == c:
            for d in dirs:
                if all(grid.get(p + d * i) == c for i, c in islice(enumerate(xmas), 1, None)):
                    n += 1
    print(n)

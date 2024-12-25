from adventlib import readgrid
from diapyr.util import bfs

plus = (1, 0), (0, 1), (-1, 0), (0, -1)

def getregion(grid):
    p, c = next(iter(grid.items()))
    @bfs([p])
    def proc(info, p):
        for d in plus:
            q = p + d
            if c == grid.get(q):
                yield q
    return proc.donekeys

def main():
    grid = {}
    for p, c in readgrid():
        grid[p] = c
    grid2 = grid.copy()
    regions = []
    while grid2:
        regions.append(getregion(grid2))
        for p in regions[-1]:
            grid2.pop(p)
    n = 0
    for region in regions:
        plant = grid[next(iter(region))]
        fence = 0
        for p in region:
            for d in plus:
                fence += plant != grid.get(p + d)
        n += len(region) * fence
    print(n)
